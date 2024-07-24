from abc import ABC, abstractmethod

class InteractivityMixin(ABC):
    
    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError("Method validate must be implemented")

    interactive: bool

    @staticmethod
    def setInteractive(interactive: bool) -> None:
        InteractivityMixin.interactive = interactive

    def default(self):
        default = self.value()

        self.validate(default)

        if self.state == 'error':
            raise ValueError("Default value is invalid")
        
        return default