from copy import deepcopy
from typing import List
from enums.EnumTipoCelula import EnumTipoCelula
from estruturas.celulas.CelulaV1 import CelulaV1
from interfaces.InterfaceLista import InterfaceLista
from interfaces.InterfaceTeste import InterfaceTeste
from estruturas.listas.ListaContigua import ListaContigua
from estruturas.listas.ListaEncadeadaV1 import ListaEncadeadaV1
from estruturas.listas.ListaEncadeadaV2 import ListaEncadeadaV2
from estruturas.listas.ListaEncadeadaV3 import ListaEncadeadaV3
from estruturas.listas.ListaEncadeadaV4 import ListaEncadeadaV4

class TesteListas(InterfaceTeste):
    def __init__(self):
        pass

    def inicializar(self,listas:List[InterfaceLista]):
        lista_teste = [0,1,2,3,4]
        for lista in listas:
            l = [item.chave for item in lista.toList()]
            assert(l == lista_teste)

    def remocaoInicioEmListasComMaisDe1Item(self):
        listas : List[InterfaceLista]= [
                                        # ListaContigua[int](1),
                                        ListaEncadeadaV1[int](5),
                                        ListaEncadeadaV2[int](5),
                                        ListaEncadeadaV3[int](5),
                                        ListaEncadeadaV4[int](5),
                                        ]
        l = []
        for lista in listas:
            lista.zerarAcessos()
            lista.removerInicio(0)
            l.append(lista.quantidadeAcessos)
        assert(l == [3,3,4,8])
    def remocaoInicioListaCom1Item(self):
        listas : List[InterfaceLista]= [
                                        # ListaContigua[int](1),
                                        ListaEncadeadaV1[int](1),
                                        ListaEncadeadaV2[int](1),
                                        ListaEncadeadaV3[int](1),
                                        ListaEncadeadaV4[int](1),
                                        ]
        
        l = []
        for lista in listas:
            lista.zerarAcessos()
            lista.removerInicio(0)
            l.append(lista.quantidadeAcessos)
        assert(l == [2,3,4,5])

        pass
    # def remocaoFinal(self,listas:List[InterfaceLista]):
    #     lista_teste = [0,1,2,3]
    #     for lista in deepcopy(listas):
    #         lista.remover()
    #         l = [item.chave for item in lista.toList()]
    #         assert(l == lista_teste)
        
    #     lista_teste = [0,1,2,3,4]
    #     for lista in deepcopy(listas):
    #         lista.remover()
    #         lista.remover()
    #         lista.remover()
    #         lista.remover()
    #         lista.remover()
    #         l = [item.chave for item in lista.toList()]
    #         assert(lista.toList() == [])



    def remocaoInicio(self,listas:List[InterfaceLista]):
        lista_teste = [1,2,3,4]
        # for lista in deepcopy(listas):
        #     lista.removerInicio(0)
        #     l = [item.chave for item in lista.toList()]
        #     assert(l == lista_teste)
        for lista in deepcopy(listas):
            # lista.print()
            lista.removerInicio(0)
            # lista.print()
            lista.removerInicio(0)
            # lista.print()
            lista.removerInicio(0)
            # lista.print()
            lista.removerInicio(0)
            # lista.print()
            lista.removerInicio(0)
            # lista.print()
            l = [item.chave for item in lista.toList()]
            # print(l)
            assert(l == [])
        
    def run(self):
        listas : List[InterfaceLista]= [
                                        ListaEncadeadaV1[int](5),
                                        ListaEncadeadaV2[int](5),
                                        ListaEncadeadaV3[int](5),
                                        ListaEncadeadaV4[int](5),
                                        ]

        # self.inicializar(deepcopy(listas))
        # self.remocaoFinal(deepcopy(listas))
        self.remocaoInicio(deepcopy(listas))
        # self.remocaoInicioEmListasComMaisDe1Item()
        # self.remocaoInicioListaCom1Item()
 