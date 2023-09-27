from typing import TypeVar
from interfaces.InterfaceFila import InterfaceFila
from interfaces.InterfaceLista import InterfaceLista

T = TypeVar('T')

class FilaListaEncadeada(InterfaceFila):
    def __init__(self, lista : InterfaceLista,nome : str):
        self._lista = lista
        self._nome = nome
        # inicio é o mesmo que self._primeiroItem
        # fim é o mesmo que self.quantidadeElementos
    def enfileirar(self, elemento : T):
        # indice == None == inserir no final
        self._lista.inserir(elemento = elemento, indice = None)

    @property
    def nome(self):
        return self._nome
    
    def desenfileirar(self) -> T:
        return self._lista.remover(0)

    def toList(self,) -> list:
        return self._lista.toList()
    
    def print(self):
        self._lista.print()

    def zerarAcessos(self):
        self._lista.zerarAcessos()
    @property
    def quantidadeAcessos(self):
        return self._lista.quantidadeAcessos
        