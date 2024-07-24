import re
from typing import List

class TruncateMixin:

    def truncate(self, string: str, width: int) -> str:
        """Truncates a string with an ellipsis if it exceeds the given width."""
        if width <= 0:
            raise ValueError(f"Width [{width}] must be greater than zero.")

        if len(string) <= width:
            return string
        else:
            return string[:width - 1] + '…'  # Use slicing for efficient truncation

    def mb_wordwrap(self, string: str, width: int = 75, break_char: str = "\n", cut_long_words: bool = False) -> str:
        """Multi-byte aware word wrap function."""
        lines = string.split(break_char)
        result: List[str] = []

        for original_line in lines:
            if len(original_line) <= width:
                result.append(original_line)
                continue

            words = original_line.split(' ')
            line = ""
            line_width = 0

            if cut_long_words:
                for i, word in enumerate(words):
                    characters = list(word)  # Split word into characters
                    split_words = []
                    current_word = ""

                    for char in characters:
                        temp = current_word + char
                        if len(temp) > width:
                            split_words.append(current_word)
                            current_word = char
                        else:
                            current_word = temp

                    if current_word:
                        split_words.append(current_word)

                    words[i] = " ".join(split_words)  # Rebuild the word

                words = " ".join(words).split(' ')  # Flatten the split words

            for word in words:
                temp = word if line == "" else line + " " + word  # Add space if not the first word

                # Check for zero-width joiners (combined emojis) using regex
                joiner_matches = re.findall(r'\p{Cf}', word) 

                word_width = 2 if joiner_matches else len(word)  # Account for joiner width
                line_width += word_width

                if line != "":  # Add space width if not the first word on the line
                    line_width += 1

                if line_width <= width:
                    line = temp
                else:
                    result.append(line)
                    line = word
                    line_width = word_width

            if line:  # Add the last line if it's not empty
                result.append(line)

        return break_char.join(result)  # Join the lines back with the break character