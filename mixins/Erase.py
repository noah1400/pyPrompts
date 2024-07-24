from abc import ABC, abstractmethod

class EraseMixin(ABC):

    @abstractmethod
    def writeDirectly(self, text: str) -> None:
        raise NotImplementedError("Method writeDirectly must be implemented")
    
    def eraseLines(self, count: int) -> None:
        clear = ''
        for i in range(count):
            clear += f"\033[2K{'\033[1A' if i < count - 1 else ''}"

        if count > 0:
            clear += '\033[G'

        self.writeDirectly(clear)

    def eraseDown(self) -> None:
        self.writeDirectly("\033[J")