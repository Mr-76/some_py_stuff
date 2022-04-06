#testando herdar metodos da classe list

class ListaCompra(list):
    def __init__(mulo,nome_lista,lista):
        mulo._nome = nome_lista
        super().__init__(lista)
        mulo._lista = lista
    def __repr__(mulo):
        """ Printa string como representaçao do obj"""
        return ("ListaCompra({},{}).".format(mulo._nome,mulo._lista))

coisas = ["feijao","arroz","carne"]

compra = ListaCompra("Comprar HJ",coisas)


for i in compra:
    print(i)
a = 0

#infinitozaooo
for i in range(10):
    compra.append(a)
    print(i)
    a+=1
print(compra)

help(compra) #ver help do arquivo com mudanças



