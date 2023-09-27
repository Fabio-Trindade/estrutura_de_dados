from copy import deepcopy
from typing import Generic, TypeVar, List
from estruturas.Item import Item
from interfaces.InterfaceLista import InterfaceLista
T = TypeVar('T')

class ListaContigua(InterfaceLista,Generic[T]):
    def __init__(self, tamanho:int):
        super().__init__()
        self._tamanho = tamanho
        self._lista : List[T] =  [Item(i) for i in range(tamanho)]
        self.setQuantidadeElementos(tamanho)

    def inserirMeio(self, elemento: T, indice: int) -> bool:
        for i in range(self.quantidadeElementos, indice, -1):
            self.contarAcesso()
            self._lista[i] = self._lista[i-1]
        self.contarAcesso()
        self._lista[indice] = elemento
        return True
    
    def inserirFinal(self, elemento: T) -> bool:
        self.contarAcesso()
        self._lista[self.quantidadeElementos] = elemento
        return True
    
    def inserirInicio(self, elemento: T) -> bool:
        return self.inserirMeio(elemento, 0)
    
    def removerMeio(self, indice: int) -> T:
        self.contarAcesso()
        aux = self._lista[indice]
        for i in range(indice,self.quantidadeElementos-1):
            self.contarAcesso()
            self._lista[i] = self._lista[i + 1]
        return aux
    
    def removerInicio(self, indice: int = 0) -> T:
        return self.removerMeio(0)
    
    def removerFinal(self, indice : int = None) -> T:
        self.contarAcesso()
        return self._lista[self.quantidadeElementos-1]
    
    def cheia(self) -> bool:
        return self._tamanho == self.quantidadeElementos 

    def print(self, indice = 0):
        for item in self._lista[indice:self.quantidadeElementos]:
            print(item.chave, end = ' ')

    def toList(self,indice = 0) -> list:
        return deepcopy(self._lista[indice:self.quantidadeElementos])

