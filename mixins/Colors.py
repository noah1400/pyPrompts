
class ColorsMixin():

    def reset(self, text: str) -> str:
        return f"\033[0m{text}\033[0m"
    
    def bold(self, text: str) -> str:
        return f"\033[1m{text}\033[22m"
    
    def dim(self, text: str) -> str:
        return f"\033[2m{text}\033[22m"
    
    def italic(self, text: str) -> str:
        return f"\033[3m{text}\033[23m"
    
    def underline(self, text: str) -> str:
        return f"\033[4m{text}\033[24m"
    
    def inverse(self, text: str) -> str:
        return f"\033[7m{text}\033[27m"
    
    def hidden(self, text: str) -> str:
        return f"\033[8m{text}\033[28m"
    
    def strikethrough(self, text: str) -> str:
        return f"\033[9m{text}\033[29m"
    
    def black(self, text: str) -> str:
        return f"\033[30m{text}\033[39m"
    
    def red(self, text: str) -> str:
        return f"\033[31m{text}\033[39m"
    
    def green(self, text: str) -> str:
        return f"\033[32m{text}\033[39m"
    
    def yellow(self, text: str) -> str:
        return f"\033[33m{text}\033[39m"
    
    def blue(self, text: str) -> str:
        return f"\033[34m{text}\033[39m"
    
    def magenta(self, text: str) -> str:
        return f"\033[35m{text}\033[39m"
    
    def cyan(self, text: str) -> str:
        return f"\033[36m{text}\033[39m"
    
    def white(self, text: str) -> str:
        return f"\033[37m{text}\033[39m"
    
    def bgBlack(self, text: str) -> str:
        return f"\033[40m{text}\033[49m"
    
    def bgRed(self, text: str) -> str:
        return f"\033[41m{text}\033[49m"
    
    def bgGreen(self, text: str) -> str:
        return f"\033[42m{text}\033[49m"
    
    def bgYellow(self, text: str) -> str:
        return f"\033[43m{text}\033[49m"
    
    def bgBlue(self, text: str) -> str:
        return f"\033[44m{text}\033[49m"
    
    def bgMagenta(self, text: str) -> str:
        return f"\033[45m{text}\033[49m"
    
    def bgCyan(self, text: str) -> str:
        return f"\033[46m{text}\033[49m"
    
    def bgWhite(self, text: str) -> str:
        return f"\033[47m{text}\033[49m"
    
    def gray(self, text: str) -> str:
        return f"\033[90m{text}\033[39m"

