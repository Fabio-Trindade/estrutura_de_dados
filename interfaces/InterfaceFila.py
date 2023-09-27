from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from interfaces.InterfaceLista import InterfaceLista
class InterfaceFila(ABC,):
    def __init__(self, lista : InterfaceLista):
        pass      
      
    def enfileirar(self):
        pass
    
    def desenfileirar(self) :
        pass

    def toList(self) -> list:
        pass

