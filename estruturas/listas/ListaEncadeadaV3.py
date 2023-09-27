from typing import Generic, TypeVar
from enums.EnumTipoCelula import EnumTipoCelula
from interfaces.InterfaceCelula import Celula
from estruturas.listas.ListaEncadeadaV2 import ListaEncadeadaV2
T = TypeVar('T')


class ListaEncadeadaV3(ListaEncadeadaV2,Generic[T]):
    def __init__(self, tamanho: int, tipoCelula = EnumTipoCelula.CELULAV1):
        super().__init__(tamanho,tipoCelula )
        self._primeiroItem = self.criarCelula(None)
        p, u =super().inicializar()
        self._primeiroItem.setProximo(p)
        self._primeiroItem.proximo.setAnterior(self._primeiroItem)
        self._ultimoItem = u
    
    def inserirFinal(self, elemento: T) -> bool:
        penultimoItem = self._ultimoItem
        # self.contarAcesso()
        self._ultimoItem = self.criarCelula(elemento)
        # self.contarAcesso()
        penultimoItem.setProximo(self._ultimoItem)
        # self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        self._ultimoItem.setAnterior(penultimoItem)
        return True
    
    def inserirInicio(self, elemento: T) -> bool:
        # self.contarAcesso()
        self._primeiroItem.setItem(elemento)
        proximo = self._primeiroItem
        # self.contarAcesso()
        self._primeiroItem = self.criarCelula(None)
        # self.contarAcesso()
        self._primeiroItem.setProximo(proximo)
        # self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        proximo.setAnterior(self._primeiroItem)
        return True
    
    def inserirMeio(self, elemento: T, indice: int):
        return super().inserirMeio(elemento, indice + 1)
    
    def removerMeio(self, indice: int) -> T:
        return super().removerMeio(indice + 1)
    
    def removerInicio(self, indice: int = 0) -> T:
        self.contarAcesso()
        atual = self._primeiroItem.proximo
        self.contarAcesso(2)
        self._primeiroItem.setProximo(atual.proximo)
        if self.quantidadeElementos == 1:
            self.contarAcesso()
            self._ultimoItem = self._primeiroItem
        else:
            self.contarAcesso(1)
            atual.setProximo(None)
            self.contarAcesso(3 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0)
            self._primeiroItem.proximo.setAnterior(atual.anterior)
        self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        atual.setAnterior(None)
        # self.diminuirQuantidadeElementos()
        return atual.item
    
    def removerFinal(self, indice : int = None):
        prox : Celula = self._primeiroItem
        for i in range(self.quantidadeElementos - 1):
            self.contarAcesso()
            prox = prox.proximo
        self.contarAcesso()
        item = prox.proximo
        self.contarAcesso()
        prox.setProximo(None)
        self.contarAcesso()
        self._ultimoItem = prox
        return item.item
    
    def print(self,):
        prox : Celula = self._primeiroItem.proximo
        while  prox != None:
            print(str(prox.item.chave) + " -> ", end= '')
            prox = prox.proximo
        
    def toList(self) -> list:
        lista = []
        prox = self._primeiroItem.proximo
        while  prox != None:
            lista.append(prox.item)
            prox = prox.proximo
        return lista
