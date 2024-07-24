from Prompt import Prompt
from mixins import TypedValueMixin

class TextPrompt(Prompt,TypedValueMixin):
    
    def __init__(self, label: str, placeholder: str = '', default: str = '', required: bool|str = False, validate = None, hint: str = ''):
        TypedValueMixin.__init__(self)
        Prompt.__init__(self)
        self.label = label
        self.placeholder = placeholder
        self.default = default
        self.required = required
        self.validate = validate
        self.hintStr = hint
        self.trackTypedValue(default)

    def valueWithCursor(self, max_width: int):
        if self.value() == '':
            return self.dim(self.addCursor(self.placeholder, 0, max_width))

        return self.addCursor(self.value(), self.cursorPosition, max_width)
    
    def value(self) -> str:
        return super().value()