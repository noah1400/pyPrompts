import re
from typing import List


class InteractsWithStringsMixin:

    def longest(self, lines: List[str], padding: int = 0) -> int:
        """Calculates the length of the longest line, ignoring escape sequences."""
        longest_length = self.min_width
        for line in lines:
            stripped_line = self.strip_escape_sequences(line)
            longest_length = max(longest_length, len(stripped_line) + padding)
        return longest_length

    def pad(self, text: str, length: int, char: str = ' ') -> str:
        """Pads text to the given length, ignoring escape sequences."""
        stripped_text = self.strip_escape_sequences(text)
        padding_length = max(0, length - len(stripped_text))
        return text + char * padding_length 

    def strip_escape_sequences(self, text: str) -> str:
        """Removes ANSI escape sequences and Symfony style tags from text."""
        # Strip ANSI escape sequences
        text = re.sub(r"\x1b[^m]*m", '', text) 

        # Strip Symfony named style tags
        text = re.sub(r"<(info|comment|question|error)>(.*?)</\1>", r'\2', text)

        # Strip Symfony inline style tags
        text = re.sub(r"<(?:(?:[fb]g|options)=[a-z,;]+)+>(.*?)</>", r'\1', text, flags=re.IGNORECASE)

        return text