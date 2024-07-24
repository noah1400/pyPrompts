from abc import ABC, abstractmethod

class FallbackMixin(ABC):

    @abstractmethod
    def getOwnClassName(self) -> str:
        raise NotImplementedError("Method getOwnClassName must be implemented")
    
    shouldFallback = False

    fallbacks = {}

    @staticmethod
    def fallbackWhen(condition: bool) -> None:
        FallbackMixin.shouldFallback = condition or FallbackMixin.shouldFallback

    @staticmethod
    def getShouldFallback() -> bool:
        return FallbackMixin.shouldFallback and FallbackMixin.fallbacks[FallbackMixin.getOwnClassName()] is not None
    
    @staticmethod
    def fallbackUsing(fallback: callable) -> None:
        FallbackMixin.fallbacks[FallbackMixin.getOwnClassName()] = fallback

    def fallback(self):
        fallback = FallbackMixin.fallbacks[FallbackMixin.getOwnClassName()]
        if fallback is None:
            raise RuntimeError(f"Method {FallbackMixin.getOwnClassName()} has no fallback")
        
        return fallback(self)