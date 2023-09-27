from abc import ABC, abstractmethod, ABCMeta
from typing import TypeVar

T = TypeVar("T")

class InterfaceLista(ABC):
    def __init__(self):
        self._quantidadeElementos = 0
        self._contador = 0

    def setQuantidadeElementos(self, tamanho: int):
        self._quantidadeElementos = tamanho 

    def contarAcesso(self, acessos = 1):
        self._contador += acessos

    @property
    def quantidadeAcessos(self):
        return self._contador

    def zerarAcessos(self):
        self._contador = 0
    
    def printAcessos(self):
        print("Quantidade de acessos realizados:", self._contador)

    def inserir(self, elemento: T, indice:int = None) -> bool:
        if self.cheia():
            print("ERRO: Lista Cheia!")
            return False
        elif indice != None and not self.posicaoEhValida(indice) :
            print("ERRO: Posição inválida!")
            return False
        bool = False
        if indice == 0:
            bool = self.inserirInicio(elemento)
        elif indice == None or indice  ==  self.quantidadeElementos :
            bool = self.inserirFinal(elemento)
        else:
            bool = self.inserirMeio(elemento, indice)
        self.__aumentarQuantidadeElementos()
        return bool
    
    @abstractmethod
    def inserirMeio(self, elemento: T, indice:int) -> bool:
        pass

    @abstractmethod
    def inserirFinal(self, elemento: T, indice: int) -> bool:
        pass

    @abstractmethod
    def inserirInicio(self, elemento: T, indice: int) -> bool:
        pass

    def remover(self, indice: int = None) -> T:
        if self.vazia():
            print("ERRO: Lista vazia!")
            return None
        elif not self.posicaoEhValida(indice):
            print ("ERRO: Posição inválida!")
            return None
        if indice == 0:
            elemento = self.removerInicio(indice)
        elif indice == None or indice + 1 ==  self.quantidadeElementos:
            elemento = self.removerFinal(indice)
        else:
            elemento = self.removerMeio( indice)
        self.diminuirQuantidadeElementos()
        return elemento
    
    @abstractmethod
    def removerMeio(self, indice:int = None) -> T:
        pass
    @abstractmethod
    def removerInicio(self, indice : int = None) -> T:
        pass
    @abstractmethod
    def removerFinal(self, indice : int = None) -> T:
        pass

    
    def vazia(self) -> bool:
        return self.quantidadeElementos == 0
    
    @abstractmethod
    def cheia(self, quantidade: int = None) -> bool:
        pass
    
    def print(self):
        pass
    
    def toList(self) -> list:
        pass

    def posicaoEhValida(self, indice) -> bool:
        if indice == None:
            return True
        return not(indice > self.quantidadeElementos or indice < 0)
    
    @property
    def quantidadeElementos(self) -> int:
        return self._quantidadeElementos

    def aumentarQuantidadeElementos(self) -> None:
        self._quantidadeElementos += 1

    def diminuirQuantidadeElementos(self) -> None:
        self._quantidadeElementos -= 1
