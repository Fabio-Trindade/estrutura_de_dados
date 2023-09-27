from abc import ABC, abstractmethod
from typing import Generic, TypeVar
T = TypeVar('T')

class Celula(ABC,Generic[T]):
    def __init__(self, item : T):
        self._item : T = item

    @property
    def item(self) -> T:
        return self._item
    
    @property
    def proximo(self) :
        pass

    @property
    def anterior(self):
        pass

    @abstractmethod
    def setProximo(self, proximo) :
        pass
    @abstractmethod
    def setAnterior(self, anterior) :
        pass

    def setItem(self, item: T):
        self._item = item
    
    def setApontadores(self, celulaAnterior, celulaPosterior):
        self.setAnterior(celulaAnterior)
        self.setProximo(celulaPosterior)