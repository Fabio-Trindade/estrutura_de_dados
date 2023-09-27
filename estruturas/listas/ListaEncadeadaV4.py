from typing import Generic, TypeVar
from enums.EnumTipoCelula import EnumTipoCelula
from interfaces.InterfaceCelula import Celula
from estruturas.listas.ListaEncadeadaV3 import ListaEncadeadaV3
T = TypeVar('T')


class ListaEncadeadaV4(ListaEncadeadaV3,Generic[T]):
    def __init__(self, tamanho : int,tipoCelula = EnumTipoCelula.CELULAV2):
        super().__init__(tamanho,tipoCelula)
        
    def removerFinal(self, indice : int = None) -> T:
        item = self._ultimoItem
        self.contarAcesso()
        anterior = self._ultimoItem.anterior
        self.contarAcesso()
        anterior.setProximo(None)
        self.contarAcesso()
        self._ultimoItem = anterior
        return item
    
    def toListReverso(self):
        lista = []
        prox = self._ultimoItem
        while  prox != None:
            if prox.item != None:
                lista.append(prox.item.chave)
            prox = prox.anterior
        return lista