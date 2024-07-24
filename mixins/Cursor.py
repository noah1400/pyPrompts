from abc import ABC, abstractmethod

class CursorMixin(ABC):

    cursorHidden = False

    @abstractmethod
    def writeDirectly(self, text: str) -> None:
        raise NotImplementedError("Method writeDirectly must be implemented")
    
    def hideCursor(self) -> None:
        self.writeDirectly("\033[?25l")
        self.cursorHidden = True

    def showCursor(self) -> None:
        self.writeDirectly("\033[?25h")
        self.cursorHidden = False

    def restoreCursor(self) -> None:
        if self.cursorHidden:
            self.showCursor()

    def moveCursor(self, x: int, y: int) -> None:
        sequence = ''
        if x < 0:
            sequence += f"\033[{abs(x)}D" # Left
        elif x > 0:
            sequence += f"\033[{x}C" # Right

        if y < 0:
            sequence += f"\033[{abs(y)}A" # Up
        elif y > 0:
            sequence += f"\033[{y}B" # Down

        self.writeDirectly(sequence)

    def moveCursorToColumn(self, x: int) -> None:
        self.writeDirectly(f"\033[{x}G")

    def moveCursorUp(self, lines: int) -> None:
        self.writeDirectly(f"\033[{lines}A")