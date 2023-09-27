from testes.filas.TesteFilas import TesteFilas
from testes.listas.TesteListas import TesteListas

testes = [TesteListas(),TesteFilas() ]
for teste in testes:
    teste.run()

# from listas.ListaContigua import ListaContigua


# l = ListaContigua[int](5)
# l.inserir(2)
# print(l.quantidadeElementos)
# l.print()