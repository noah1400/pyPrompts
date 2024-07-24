from renderer import Renderer
from renderer.TextPromptRenderer import TextPromptRenderer
from abc import ABC, abstractmethod

class ThemesMixin(ABC):

    theme: str = 'default'

    themes = {
        'default': {
            'TextPrompt': TextPromptRenderer
        }
    }

    @staticmethod
    def themeFor(name: str|None) -> str:
        if name is None:
            return ThemesMixin.theme 
        
        if ThemesMixin.themes.get(name) is None:
            raise Exception(f"Theme {name} not found")
        
        ThemesMixin.theme = name

        return ThemesMixin.theme
    
    def getRenderer(self) -> Renderer:
        className = self.getOwnClassName()

        if ThemesMixin.themes[ThemesMixin.theme].get(className) is None:
            raise Exception(f"Renderer for {className} not found in theme {ThemesMixin.theme}")
        
        return ThemesMixin.themes[ThemesMixin.theme][className](self)
    
    def renderTheme(self):
        renderer = self.getRenderer()

        return renderer(self)
        