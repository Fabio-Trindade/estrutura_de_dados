import csv
from estruturas.Dicionario import Dicionario
from estruturas.FilaListaContigua import FilaListaContigua
from estruturas.FilaListaEncadeada import FilaListaEncadeada
from estruturas.Item import Item
from estruturas.listas.ListaEncadeadaV1 import ListaEncadeadaV1
from estruturas.listas.ListaEncadeadaV2 import ListaEncadeadaV2
from estruturas.listas.ListaEncadeadaV3 import ListaEncadeadaV3
from estruturas.listas.ListaEncadeadaV4 import ListaEncadeadaV4

with open('csvs/dados_pior_caso.csv',mode='w',encoding='utf-8',newline='') as nome_arquivo:
    file_csv = csv.writer(nome_arquivo,delimiter=',')
    file_csv.writerow(['Fila',"n","C(n)"])
    for i in range(0,10000):
        fila = FilaListaContigua[Item](i)
        dic = Dicionario(i,fila)
        indice, acessos = dic.pesquisar(i+1)
        file_csv.writerow([fila.nome,str(i),str(acessos)])
        for lista,nome in [
            (ListaEncadeadaV1[Item](i),'FLEV1'),
                    (ListaEncadeadaV2[Item](i),'FLEV2'),
                    (ListaEncadeadaV3[Item](i),'FLEV3'),
                    (ListaEncadeadaV4[Item](i),'FLEV4'),
                                                            ]:
            fila = FilaListaEncadeada(lista,nome)
            dic = Dicionario(i,fila)
            indice, acessos = dic.pesquisar(i+1)
            file_csv.writerow([fila.nome,str(i),str(acessos)])

with open('csvs/dados_melhor_caso.csv',mode='w',encoding='utf-8',newline='') as nome_arquivo:
    file_csv = csv.writer(nome_arquivo,delimiter=',')
    file_csv.writerow(['Fila',"n","C(n)"])
    for i in range(0,10000):
        fila = FilaListaContigua[Item](i)
        dic = Dicionario(i,fila)
        indice, acessos = dic.pesquisar(0)
        file_csv.writerow([fila.nome,str(i),str(acessos)])
        for lista,nome in [
            (ListaEncadeadaV1[Item](i),'FLEV1'),
                    (ListaEncadeadaV2[Item](i),'FLEV2'),
                    (ListaEncadeadaV3[Item](i),'FLEV3'),
                    (ListaEncadeadaV4[Item](i),'FLEV4'),
                                                            ]:
            fila = FilaListaEncadeada(lista,nome)
            dic = Dicionario(i,fila)
            indice, acessos = dic.pesquisar(0)
            file_csv.writerow([fila.nome,str(i),str(acessos)])
