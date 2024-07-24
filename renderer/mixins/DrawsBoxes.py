from .InteractsWithStrings import InteractsWithStringsMixin
from typing import List, Callable

class DrawsBoxesMixin(InteractsWithStringsMixin):
    
    def __init__(self):
        self.min_width = 60

    def box(self, title: str, body: str, footer: str = '', color: str = 'gray', info: str = '', prompt = None):
        """Draws a box around text with optional title, footer, and info."""

        terminal_width = prompt.getTerminal().cols()
        self.min_width = min(self.min_width, terminal_width - 6)

        body_lines = body.splitlines()
        footer_lines = [line for line in footer.splitlines() if line.strip()] 

        lines = body_lines + footer_lines + [title]
        width = self.longest(lines)

        title_length = len(self.strip_escape_sequences(title))
        title_label = f" {title} " if title_length > 0 else ""
        top_border = "─" * (width - title_length + (0 if title_length > 0 else 2))

        color_func: Callable[[str], str] = getattr(self, color, lambda x: x)  # Get color function or default to no color
        
        # Call the color function dynamically on each part of the line:
        self.line(f"{color_func(' ┌')}{title_label}{color_func(top_border + '┐')}")

        for line in body_lines:
            self.line(f"{color_func(' │')} {self.pad(line, width)} {color_func('│')}")

        if footer_lines:
            self.line(f"{color_func(' ├')}{color_func('─' * (width + 2))}┤")
            for line in footer_lines:
                self.line(f"{color_func(' │')} {self.pad(line, width)} {color_func('│')}")

        info_width = 0 if not info else len(self.strip_escape_sequences(info))
        bottom_border = "─" * (width - info_width if info else width + 2)
        info_label = f" {info} " if info else ""
        self.line(f"{color_func(' └')}{bottom_border}{info_label}{color_func('┘')}")

        return self