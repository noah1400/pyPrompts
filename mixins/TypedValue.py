from abc import ABC, abstractmethod
from Key import Key
from typing import List

class TypedValueMixin(ABC):

    @abstractmethod
    def on(self, event: str, callback: callable):
        pass
    
    def __init__(self):
        self.typedValue: str = ''
        self.cursorPosition: int = 0

    def trackTypedValueOnKey(self, key: tuple|List[tuple], shouldSubmit: bool, ignore: callable, allowNewLine: bool):
        if key[0] == b'\x00' or key in [Key.CTRL_B, Key.CTRL_F, Key.CTRL_A, Key.CTRL_E]:
            if ignore is not None and ignore(key):
                return
            
            if key in [Key.LEFT, Key.LEFT_ARROW, Key.CTRL_B]:
                self.cursorPosition = max(0, self.cursorPosition - 1)
            elif key in [Key.RIGHT, Key.RIGHT_ARROW, Key.CTRL_F]:
                self.cursorPosition = min(len(self.typedValue), self.cursorPosition + 1)
            elif key in [Key.HOME, Key.CTRL_A]:
                self.cursorPosition = 0
            elif key in [Key.END, Key.CTRL_E]:
                self.cursorPosition = len(self.typedValue)
            elif key == Key.DELETE:
                self.typedValue = self.typedValue[:self.cursorPosition] + self.typedValue[self.cursorPosition + 1:]
            self.render()
            return
        
        if isinstance(key, tuple):
            key = [key]
        for k in key:
            if ignore is not None and ignore(k):
                return
            if k == Key.ENTER:
                if shouldSubmit:
                    self.submit()
                    self.render()
                    return
                if allowNewLine:
                    self.typedValue = self.typedValue[:self.cursorPosition] + '\n' + self.typedValue[self.cursorPosition:]
                    self.cursorPosition += 1
            elif k == Key.BACKSPACE:
                if self.cursorPosition == 0:
                    return
                self.typedValue = self.typedValue[:self.cursorPosition - 1] + self.typedValue[self.cursorPosition:]
                self.cursorPosition -= 1
            elif ord(k[0]) >= 32 and ord(k[0]) <= 126:
                self.typedValue = self.typedValue[:self.cursorPosition] + k[0].decode('utf-8') + self.typedValue[self.cursorPosition:]
                self.cursorPosition += 1

            self.render()

    def trackTypedValue(self, default: str = '', submit: bool = True, ignore: callable = None, allowNewLine: bool = False):
        self.typedValue = default
        if self.typedValue:
            self.cursorPosition = len(self.typedValue)

        self.on('key', lambda key: self.trackTypedValueOnKey(key, submit, ignore, allowNewLine))

    def value(self):
        return self.typedValue
    
    def addCursor(self, value: str, cursor_position: int, max_width: int | None = None) -> str:
        before = value[:cursor_position]  
        current = value[cursor_position] if cursor_position < len(value) else ""  
        after = value[cursor_position + 1:]  
        cursor = current if current != "\n" and current != "" else " "  

        # Calculate space available
        if max_width is None or max_width < 0:
            space_before = len(before)
            space_after = len(after)
        else:
            available_space = max_width - len(cursor)
            space_before = min(available_space, len(before))  
            space_after = available_space - space_before

        # Truncate before and after
        truncated_before = before[-space_before:]
        truncated_after = after[:space_after]

        # Mark the cursor position
        cursor_marker = self.inverse(cursor)

        # Combine the parts
        return (
            (self.dim("…") if len(before) > space_before else "") +
            truncated_before +
            cursor_marker +
            ("\n" if current == "\n" else "") +
            truncated_after +
            (self.dim("…") if len(after) > space_after else "")
        )
    
    def trim_width_backwards(self, text: str, max_width: int) -> str:
        """Trims the text to a maximum width, starting from the end."""
        if len(text) <= max_width:
            return text

        trimmed = ""
        for char in reversed(text):
            if len(trimmed) + 1 > max_width:
                break  # Stop when exceeding max_width
            trimmed = char + trimmed
        return trimmed