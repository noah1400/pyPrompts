
from renderer.Renderer import Renderer
from renderer.mixins.DrawsBoxes import DrawsBoxesMixin


class TextPromptRenderer(Renderer, DrawsBoxesMixin):

    def __init__(self, prompt) -> None:
        Renderer.__init__(self, prompt)
        DrawsBoxesMixin.__init__(self)

    def __call__(self, prompt) -> str:
        max_width = prompt.getTerminal().cols() - 6

        if prompt.state == 'submit':
            return self.box(
                self.dim(self.truncate(prompt.label, prompt.getTerminal().cols() - 6)),
                self.truncate(prompt.value(), max_width),
                prompt= prompt,
            )
        elif prompt.state == 'cancel':
            result = self.box(
                self.truncate(prompt.label, prompt.getTerminal().cols() - 6),
                self.strikethrough(self.dim(self.truncate(prompt.value() if prompt.value else prompt.placeholder, max_width))),
                color='red',
                prompt= prompt,
            ).error(prompt.cancelMessage)
        elif prompt.state == 'error':
            result = self.box(
                self.truncate(prompt.label, prompt.getTerminal().cols() - 6),
                prompt.valueWithCursor(max_width),
                color='yellow',
                prompt= prompt,
            ).warning(self.truncate(prompt.error, prompt.getTerminal().cols() - 5))
        else:  # Default state
            result = self.box(
                self.cyan(self.truncate(prompt.label, prompt.getTerminal().cols() - 6)),
                prompt.valueWithCursor(max_width),
                prompt= prompt,
            )
            (result.hint(prompt.hintStr) if prompt.hintStr else result.newLine())
            return result