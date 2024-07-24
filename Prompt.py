from msvcrt import getche, getch
from mixins import ColorsMixin, CursorMixin, EraseMixin, EventsMixin, FallbackMixin, InteractivityMixin, ThemesMixin
from output.ConsoleOutput import ConsoleOutput
from Terminal import Terminal
from abc import ABC, abstractmethod
from Key import Key

class Prompt(ColorsMixin, CursorMixin, EraseMixin, EventsMixin, FallbackMixin, InteractivityMixin, ThemesMixin):

    def getOwnClassName(self) -> str:
        return self.__class__.__name__

    validateUsing: callable

    revertUsing: callable

    output: ConsoleOutput

    terminal: Terminal

    def writeDirectly(self, text: str) -> None:
        self.output.writeDirectly(text)

    def __init__(self):
        ColorsMixin.__init__(self)
        CursorMixin.__init__(self)
        EraseMixin.__init__(self)
        EventsMixin.__init__(self)
        FallbackMixin.__init__(self)
        InteractivityMixin.__init__(self)
        ThemesMixin.__init__(self)

        self.state = 'initial'

        self.cancelMessage = 'Cancelled'

        self.prevFrame = ''

        self.newLinesWritten = 1

        self.required: bool 

        self.cancelUsing: callable

        self.validated: bool = False

        self.output = ConsoleOutput()

        self.terminal = Terminal()

    
    def prompt(self):
        try:
            self.capturePreviousNewLines()

            if (self.getShouldFallback()):
                self.fallback()

            self.hideCursor()

            self.render()

            while(True):
                key = self.terminal.read()
                if key is None:
                    break

                cont = self.handleKeyPress(key)

                self.render()

                if cont is False or key == Key.CTRL_C:
                    if key == Key.CTRL_C:
                        if self.cancelUsing:
                            return self.cancelUsing()
                        else:
                            return self.terminal.exit()
                        
                    if key == Key.CTRL_U and self.revertUsing:
                        raise Exception("Revert not implemented")
                    
                    return self.value()


        except Exception as e:
            raise e

        finally:
            self.clearListeners()

    def getNewLinesWritten(self) -> int:
        return self.newLinesWritten
    
    def capturePreviousNewLines(self) -> None:
        self.newLinesWritten = self.output.getNewLinesWritten()

    def render(self) -> None:
        self.terminal.initDimensions()

        frame = self.renderTheme()
        if self.state == 'initial':
            self.output.doWrite(str(frame))

            self.state = 'active'
            self.prevFrame = frame
            return
        
        terminalHeight = self.terminal.lines()
        previousFrameHeight = len(str(self.prevFrame).split('\n'))
        renderableLines = str(self.prevFrame).split('\n')[abs(min(0, terminalHeight - previousFrameHeight)):]

        self.moveCursorToColumn(1)
        self.moveCursorUp(min(terminalHeight, previousFrameHeight)-1)
        self.eraseDown()
        self.output.doWrite('\n'.join(renderableLines))

        self.prevFrame = frame

    def handleKeyPress(self, key: tuple) -> bool:

        if self.state == 'error':
            self.state = 'active'

        self.emit("key",key)

        if self.state == 'submit':
            return False
        
        if key == Key.CTRL_U:
            if not self.revertUsing:
                self.state = 'error'
                self.error = 'This field cannot be reverted'

                return True
            
            self.state = 'cancel'
            self.cancelMessage = 'Reverted'

            self.revertUsing()

            return False
        
        if key == Key.CTRL_C:
            self.state = 'cancel'
            self.cancelMessage = 'Cancelled'

            return False
        
        if self.validated:
            self.validate(self.value())

        return True

    def validate(self) -> None:
        self.validated = True
    
    def submit(self) -> None:
        # self.validate()

        if self.state == 'error':
            return
        self.state = 'submit'
    
    def getTerminal(self) -> Terminal:
        return self.terminal