from copy import deepcopy
from typing import Generic, TypeVar
from enums.EnumTipoCelula import EnumTipoCelula
from estruturas.Item import Item
from estruturas.celulas.CelulaV1 import CelulaV1
from estruturas.celulas.CelulaV2 import CelulaV2
from interfaces.InterfaceCelula import Celula
from interfaces.InterfaceLista import InterfaceLista

T = TypeVar('T')
class ListaEncadeadaV1(InterfaceLista,Generic[T]):
    def __init__(self,tamanho: int,tipoCelula = EnumTipoCelula.CELULAV1):
        super().__init__()
        self._tipoCelula : EnumTipoCelula = tipoCelula
        self._tamanho = tamanho
        self._primeiroItem : Celula[T] = self.inicializar()
        self.setQuantidadeElementos(tamanho)

            
    def inicializar(self):
        primeiro_item = self.criarCelula(Item(0))
        prox = primeiro_item
        for i in range (1, self._tamanho):
            prox.setProximo(self.criarCelula(Item(i)))
            prox = prox.proximo
        return primeiro_item

    def setTipoCelula(self, tipoCelula: EnumTipoCelula):
        self._tipoCelula = tipoCelula
    
    def criarCelula(self, elemento : T) -> Celula:
        return CelulaV1(elemento) if self._tipoCelula ==  EnumTipoCelula.CELULAV1 else CelulaV2(elemento)

    def inserirMeio(self, elemento: T, indice: int):
        prox = self._primeiroItem
        for i in range(indice - 1):
            # self.contarAcesso()
            prox = prox.proximo
        anterior = prox
        # self.contarAcesso()
        prox = prox.proximo
        atual = self.criarCelula(elemento)
        # self.contarAcesso()
        anterior.setProximo(atual)
        # self.contarAcesso(2 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 1) 
        atual.setApontadores(anterior,prox)
        return True

    def inserirInicio(self, elemento: T) -> bool:
        if self.quantidadeElementos == 0:
            # self.contarAcesso()
            self._primeiroItem =  self.criarCelula(elemento)
        else:
            proximo = self._primeiroItem
            # self.contarAcesso()
            self._primeiroItem = self.criarCelula(elemento)
            # self.contarAcesso(2 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 1) 
            self._primeiroItem.setApontadores(self._primeiroItem,proximo)
        return True
    
    def inserirFinal(self, elemento: T) -> bool:
        if self.quantidadeElementos == 0:
            return self.inserirInicio(elemento)
        return self.inserirMeio(elemento, self._quantidadeElementos)
    
    def removerMeio(self, indice: int) -> T:
        prox = self._primeiroItem
        for i in range(indice - 1):
            # self.contarAcesso()
            prox = prox.proximo
        anterior = prox
        # self.contarAcesso()
        atual = prox.proximo
        # self.contarAcesso()
        prox = atual.proximo
        # self.contarAcesso()
        anterior.setProximo(prox)
        # self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        prox.setAnterior(anterior)
        return atual.item

    def removerInicio(self, indice : int = 0) -> T:
        if self.quantidadeElementos == 1:
            item = self._primeiroItem
            self.contarAcesso(2)
            self._primeiroItem = self._primeiroItem.proximo
            # self.diminuirQuantidadeElementos()
            return item.item
        atual = self._primeiroItem
        self.contarAcesso(2)
        self._primeiroItem = self._primeiroItem.proximo
        # self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        # self._primeiroItem.setAnterior(None)
        self.contarAcesso(1)
        atual.setProximo(None)
        # self.diminuirQuantidadeElementos()
        return atual.item
    
    def removerFinal(self, indice) -> T:
        if self.quantidadeElementos == 1:
            return self.removerInicio(indice)
        prox = self._primeiroItem
        for i in range(self.quantidadeElementos - 2):
            # self.contarAcesso()
            prox = prox.proximo
        anterior = prox
        # self.contarAcesso()
        atual = prox.proximo
        # self.contarAcesso()
        prox = atual.proximo
        # self.contarAcesso()
        anterior.setProximo(prox)
        # self.contarAcesso()
        return atual.item
    
    def cheia(self, quantidade: int = None) -> bool:
        return False
    
    def print(self,):
        prox : Celula = self._primeiroItem
        while  prox != None:
            print(str(prox.item.chave) + " -> ", end= '')
            prox = prox.proximo
        
    def toList(self) -> list:
        lista = []
        prox = self._primeiroItem
        while  prox != None:
            lista.append(prox.item)
            prox = prox.proximo
        return lista
