class Conta:
    estatico = 0
    def __init__(self,titular):
        """cria objeto, titular nome do dono e extrato """
        self.__titular = titular
        self.__extrato = 100
        Conta.estatico+=1
    

    def ola(self,valor):
        self.count = valor
        return self.count

    @property #property deixa acessar o atributo como antes , o publico, metodo se escode como propriedade ?
    def extrato(self):
        return self.__extrato
   
    @extrato.setter
    def extrato(self,value):
        print("setter")
        self.__extrato = value

    @staticmethod
    def codigo():
        codigo = 10
        return codigo
    


    def __saque_ok(func):
        def innercheck(self,valor):

            if (self.__extrato >= valor):
                return func(self,valor)
            else:
                print("Impossivel")
                return False
        
        return innercheck    
    
   
    @__saque_ok
    def saca(self,valor):
        self.__extrato -= valor
        print("saque feito")
  
    def deposito(self,valor):
        self.__extrato += valor


    def transfere(self,valor,conta_destino):
        self.saca(valor);
        conta_destino.deposito(valor);

def main():
    print(Conta.codigo())
    conta1 = Conta("Corto")
    conta2 = Conta("Case")
    print(conta1.extrato)
    conta1.deposito(10)
    conta1.saca(50)
    print(conta1.extrato)
    conta1.transfere(20,conta2)
    print(conta1.extrato)
    conta1.extrato = 10
    print(conta1.extrato)
    print(conta1.ola(10)) #func cria propriedade
    conta1.count
    conta1.saca(10000)
    print(conta1.estatico)
    print(conta2.estatico)
    print(Conta.estatico)
if __name__ == '__main__':
    main()

