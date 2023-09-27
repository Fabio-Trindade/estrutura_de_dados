from random import randint
from estruturas.Item import Item
from interfaces.InterfaceFila import InterfaceFila


class Dicionario:
    def __init__(self, tamanho : int, fila : InterfaceFila) -> None:
        self._tamanho = tamanho
        # self._sentinela: Se fosse necessário acessar em 0, senão acessar (indice - 1)
        # na lista
        self.sentinela = None
        self._fila : InterfaceFila = fila

    def pesquisar(self, chave):
        self._fila.zerarAcessos()
        for i in range(self._tamanho):
            # print('i:',i)
            item : Item  = self._fila.desenfileirar()
            if item.chave == chave:
                return i, self._fila.quantidadeAcessos
        return 0, self._fila.quantidadeAcessos
    