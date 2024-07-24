import os
from msvcrt import getche, getch
from Key import Key

class Terminal:

    terminalSize: tuple[int, int]

    def lines(self) -> int:
        raise NotImplementedError("Method lines must be implemented")
    
    def initDimensions(self) -> None:
        self.terminalSize = os.get_terminal_size().lines, os.get_terminal_size().columns

    def cols(self) -> int:
        return self.terminalSize[1]
    
    def lines(self) -> int:
        return self.terminalSize[0]
    
    def read(self) -> tuple:
        key = getch()
        key = (key, )
        if (key[0] == b'\x00' or key[0] == b'\xe0'):
            key = (key[0], getch())
        return key
    
    def exit(self) -> None:
        exit(0)
