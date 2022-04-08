#testando herdar metodos da classe list

class ListaCompra():
    def __init__(mulo,nome_lista,lista):
        mulo._nome = nome_lista
       # super().__init__(lista)
        mulo._lista = lista
    
    def __getitem__(mulo,item): # trona interavel sem herdar list
        print(item)
        return mulo._lista[item]

        #nao usar junto ^^ ?
 #   def __iter__(mulo): # trona interavel sem herdar list
  #      mulo.n = mulo._lista.copy()
   #     return mulo

    #contains usar com in e not in
    # conter eh a parte que vc pergunta se exite
    # 'e' in lista       'e' ==  conter  
    def __contains__(mulo,conter):
        return True if conter in mulo._lista else False



    def __len__(mulo):
        return len(mulo._lista)

    def __repr__(mulo):
        """ Printa string como representaçao do obj"""
        return ("ListaCompra({},{}).".format(mulo._nome,mulo._lista))


    def __str__(mulo):
        return "Cria lista de compra"
    

    #ao somar os objetos oq fazer ?
    #add cuida diss
    def __add__(mulo,outro_tamanho):
        return print("Tamanho das compras",len(mulo._lista)+len(outro_tamanho._lista))
    def __sub__(mulo,outro_tamanho):
         return print("Sub do tamanho das compras",len(mulo._lista)-len(outro_tamanho._lista))
    



coisas = ["feijao","arroz","carne"]
coisas2 = ["Batata","ovo"]


compra = ListaCompra("Comprar HJ",coisas)
compra2 = ListaCompra("Comprar amanha",coisas2)


print("Printa interavel")
for i in compra:
    print(i)
a = 0


# retorna soma dos tamangos
compra + compra2

compra - compra2



print("\n")

print("tamanho de compra",len(compra))
print("\n")
print("STR do obj",compra)
print("\n")
print("REPR",repr(compra))
print("\n")

print("feijao" in compra,"\n")





