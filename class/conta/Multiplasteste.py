class Printa1:
    def __init__(mane,z):
            mane._z = z

    def printa(a):
        print(f"valor {a}")
     
class Printa3(Printa1):
    def __init__(self,b,z):
        self._b = b
        super().__init__(z)

    def printa(a):
        print(f"valor3 {a}") 
    




class Printa4:
    def printa(a):
        print(f"valor4 {a}") 


class Printa5:
    def printa(a):
        print(f"valor5 {a}")



class Printa2(Printa3):
    def __init__(sel,a,z):
        sel.a = a
        super().__init__(a,z)


    def printa1(a):
        print(f"valor2 {a}") 

a = Printa2(10,20)

print(a._b)
print(a._z)



print(Printa2.mro())


