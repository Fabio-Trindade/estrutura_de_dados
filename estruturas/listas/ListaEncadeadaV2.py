from typing import Generic, TypeVar
from enums.EnumTipoCelula import EnumTipoCelula
from estruturas.Item import Item
from interfaces.InterfaceCelula import Celula
from estruturas.listas.ListaEncadeadaV1 import ListaEncadeadaV1
T = TypeVar('T')

class ListaEncadeadaV2(ListaEncadeadaV1,Generic[T]):
    def __init__(self,tamanho: int,tipoCelula = EnumTipoCelula.CELULAV1):
        super().__init__(tamanho,tipoCelula)
        self._primeiroItem , self._ultimoItem= self.inicializar()
    
    def inicializar(self):
        primeiro_item = self.criarCelula(Item(0))
        prox = primeiro_item
        anterior = None
        for i in range (1,self._tamanho):
            prox.setProximo(self.criarCelula(Item(i)))
            prox.setAnterior(anterior)
            anterior = prox
            prox = prox.proximo
        prox.setAnterior(anterior)
        ultimo_item = prox
        return primeiro_item, ultimo_item

    def inserirInicio(self, elemento: T) -> bool:
        bool = super().inserirInicio(elemento)
        if self.quantidadeElementos == 0:
            self.contarAcesso()
            self._ultimoItem = self._primeiroItem
        return bool
    
    def inserirFinal(self, elemento: T) -> bool:
        if self.quantidadeElementos == 0:
            return self.inserirInicio(elemento)
        self.contarAcesso()
        self._ultimoItem.setProximo(self.criarCelula(elemento))
        anterior = self._ultimoItem
        self.contarAcesso()
        self._ultimoItem = self._ultimoItem.proximo
        self.contarAcesso(1 if self._tipoCelula == EnumTipoCelula.CELULAV2 else 0) 
        self._ultimoItem.setAnterior(anterior)
        return True
    
    def removerInicio(self, indice: int = None) -> T:
        item = super().removerInicio()
        if self.quantidadeElementos == 1:
            self.contarAcesso()
            self._ultimoItem = None
        return item
    
    def removerFinal(self, indice : int = None) -> T:
        if self.quantidadeElementos == 1:
            return self.removerInicio()
        else:
            prox : Celula = self._primeiroItem
            for i in range(self.quantidadeElementos - 2):
                self.contarAcesso() 
                prox = prox.proximo
            self.contarAcesso()
            item = prox.proximo
            self.contarAcesso()
            prox.setProximo(None)
            self.contarAcesso()
            self._ultimoItem = prox
            return item.item
    




