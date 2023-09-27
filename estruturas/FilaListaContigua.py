from typing import Generic, TypeVar
from estruturas.listas.ListaContigua import ListaContigua
from interfaces.InterfaceFila import InterfaceFila

T = TypeVar('T')
class FilaListaContigua(ListaContigua, InterfaceFila, Generic[T]):
    def __init__(self, tamanho: int):
        super().__init__(tamanho)
        self._inicio = 0
        self._nome = 'FLC'
        # Fim é o mesmo que self.quantidadeElementos
    @property
    def nome(self):
        return self._nome
    
    def enfileirar(self, elemento: T) -> bool:
        if self.cheia():
            print("ERRO: Lista Cheia!")
            return False
        ## indice == None == Inserir no último
        return super().inserir(elemento, indice = None)
    
    def desenfileirar(self) -> T:
        if self.vazia():
            print("ERRO: Lista vazia!")
            return None
        self._inicio += 1
        self.contarAcesso()
        return self._lista[self._inicio - 1]
    
    def print(self):
        print(self.toList())
        
    def toList(self) -> list:
        return self._lista[self._inicio:self.quantidadeElementos]