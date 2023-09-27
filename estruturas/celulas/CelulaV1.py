from typing import Generic, TypeVar

from interfaces.InterfaceCelula import Celula

T = TypeVar('T')

class CelulaV1(Celula,Generic[T]):
    def __init__(self, item:T) -> None:
        super().__init__(item)
        self._proximo : Celula = None
    
    @property
    def proximo(self) -> Celula:
        return self._proximo

    def setProximo(self,celula: Celula):
        self._proximo = celula

    def setAnterior(self, anterior):
        pass
    