from renderer import ScrollingRenderer, Renderer
from Terminal import Terminal
from abc import ABC, abstractmethod

class ScrollingMixin(ABC):

    @abstractmethod
    def getRenderer(self) -> Renderer:
        raise NotImplementedError("Method renderer must be implemented")
    
    @abstractmethod
    def terminal(self) -> Terminal:
        raise NotImplementedError("Method terminal must be implemented")

    scroll: int

    highlighted: int | None

    firstVisible: int = 0

    def initializeScrolling(self, highlighted: int | None = None) -> None:
        self.highlighted = highlighted

        self.reduceScrollingToFitTerminal()

    def reduceScrollingToFitTerminal(self) -> None:
        reservedLines = self.getRenderer().reservedLines() if isinstance(self.getRenderer(), ScrollingRenderer) else 0

        self.scroll = max(1, min(self.scroll, self.getTerminal().lines() - reservedLines))

    def highlight(self, index: int | None) -> None:
        self.highlighted = index

        if self.highlighted is None:
            return
        
        if self.highlighted < self.firstVisible:
            self.firstVisible = self.highlighted
        elif self.highlighted > self.firstVisible + self.scroll - 1:
            self.firstVisible = self.highlighted - self.scroll + 1

    def highlightPrevious(self, total: int, allowNull: bool) -> None:
        if total == 0:
            return
        
        if self.highlighted is None:
            self.highlight(total - 1)
        elif self.highlighted == 0:
            self.highlight(None if allowNull else (total - 1))
        else:
            self.highlight(self.highlighted - 1)

    def highlightNext(self, total: int, allowNull: bool) -> None:
        if total == 0:
            return
        
        if self.highlighted == total - 1:
            self.highlight(None if allowNull else 0)
        else:
            self.highlight((self.highlighted if self.highlighted is not None else -1)+1)

    def scrollToHighlighted(self, total: int) -> None:
        
        if self.highlighted < self.scroll:
            return
        
        remaining = total - self.highlighted - 1
        halfscroll = self.scroll // 2
        endOffset = max(0, halfscroll - remaining)

        if self.scroll % 2 == 0:
            endOffset -= 1

        self.firstVisible = self.highlighted - halfscroll - endOffset
