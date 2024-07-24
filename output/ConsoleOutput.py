class ConsoleOutput:
    
    newLinesWritten: int = 0

    def doWrite(self, text: str, newLine: bool = False) -> None:

        print(text, flush=True, end=('\n' if newLine else ''))

        if newLine:
            text = text + '\n'

        trailingNewLines = len(text) - len(text.rstrip('\n'))

        if text.strip() == '':
            self.newLinesWritten += trailingNewLines
        else:
            self.newLinesWritten = trailingNewLines

    def writeDirectly(self, text: str) -> None:
        self.doWrite(text)

    def getNewLinesWritten(self) -> int:
        return self.newLinesWritten
