def incrementa(x):
    print(x+1)
    return x+1



valor1 = incrementa(10)

valor2 = incrementa

valor2(10) # Faz referencia a msm funcao 

def concatena(x):
        
    x += " ALO"
    return x
def deleta(x):
    x = ""
    return x

def opera(func,texto):#funcao como parametro
    final = func(texto)
    return final


print(opera(concatena,"HELLO"))
print(opera(deleta,"HELLO"))


#funcao dentro de funcao


def cria_adder(x):
    def adder(y):
        return x+y
    return adder

add_20 = cria_adder(20)

final = add_20(20)

print(final)
