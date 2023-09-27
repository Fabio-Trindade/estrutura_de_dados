from typing import TypeVar
from estruturas.celulas.CelulaV1 import CelulaV1
from interfaces.InterfaceCelula import Celula

T = TypeVar('T')

class CelulaV2(CelulaV1):
    def __init__(self, item: T) -> None:
        super().__init__(item)
        self._anterior : Celula = None
    
    @property
    def anterior(self) -> Celula:
        return self._anterior

    def setAnterior(self,celula: Celula):
        self._anterior = celula