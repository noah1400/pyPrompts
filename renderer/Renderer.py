from mixins import ColorsMixin
from mixins.Truncate import TruncateMixin

class Renderer(ColorsMixin, TruncateMixin):

    def getOwnClassName(self) -> str:
        raise NotImplementedError("Method getOwnClassName must be implemented")

    def __init__(self, prompt) -> None:
        self.prompt = prompt
        self.output = ''

    def line(self, message: str) -> 'Renderer':
        self.output += message + '\n'
        return self
    
    def newLine(self, count: int = 1) -> 'Renderer':
        self.output += '\n' * count
        return self
    
    def warning(self, message: str) -> 'Renderer':
        return self.line(self.yellow(f"  ⚠ {message}"))
    
    def error(self, message: str) -> 'Renderer':
        return self.line(self.red(f"  ⚠ {message}"))
    
    def hint(self, message: str) -> 'Renderer':
        if message == '':
            return self

        message = self.truncate(message, self.prompt.getTerminal().cols() - 6)

        return self.line(self.gray(f"  {message}"))
    
    def when(self, value: bool, callback: callable, default: callable = None) -> 'Renderer':
        if value:
            callback(self)
        elif default:
            default(self)

        return self
    
    def __str__(self) -> str:
        return '\n' * max(2 - self.prompt.getNewLinesWritten(), 0) + self.output + ('\n' if self.prompt.state in ['submit', 'cancel'] else '')