from copy import deepcopy
from typing import List
from enums.EnumTipoCelula import EnumTipoCelula
from estruturas.FilaListaContigua import FilaListaContigua
from estruturas.FilaListaEncadeada import FilaListaEncadeada
from estruturas.Item import Item
from estruturas.celulas.CelulaV1 import CelulaV1
from interfaces.InterfaceFila import InterfaceFila
from interfaces.InterfaceLista import InterfaceLista
from interfaces.InterfaceTeste import InterfaceTeste
from estruturas.listas.ListaContigua import ListaContigua
from estruturas.listas.ListaEncadeadaV1 import ListaEncadeadaV1
from estruturas.listas.ListaEncadeadaV2 import ListaEncadeadaV2
from estruturas.listas.ListaEncadeadaV3 import ListaEncadeadaV3
from estruturas.listas.ListaEncadeadaV4 import ListaEncadeadaV4

class TesteFilas(InterfaceTeste):
    def __init__(self):
        pass
    # def enfileirar(self,filas:List[InterfaceFila]):
    #     lista_teste = [0,23,3,24]
    #     for fila in filas:
    #         for n in lista_teste:
    #             fila.enfileirar(n)
    #         assert(fila.toList() == [0,23,3,24])

    def desenfileirar(self,filas:List[InterfaceFila]):
        lista_teste = [2,3,4]
        for fila in deepcopy(filas):
            fila.desenfileirar()
            fila.desenfileirar()
            l = [item.chave for item in fila.toList()]
            assert(l == lista_teste)

        lista_teste = []
        for fila in filas:
            fila.desenfileirar()
            fila.desenfileirar()
            fila.desenfileirar()
            fila.desenfileirar()
            fila.desenfileirar()

            l = [item.chave for item in fila.toList()]
            assert(l == lista_teste)
   

    def run(self):
        filas : List[InterfaceFila]= [
                                        FilaListaContigua(5),
                                        FilaListaEncadeada(ListaEncadeadaV1(5)),
                                        FilaListaEncadeada(ListaEncadeadaV2(5)),
                                        FilaListaEncadeada(ListaEncadeadaV3(5)),
                                        FilaListaEncadeada(ListaEncadeadaV4(5))
                                        ]
        # self.enfileirar(deepcopy(filas))
        # self.desenfileirar(deepcopy(filas))
        # self.remocaoInicioFilaCom1Item()
       