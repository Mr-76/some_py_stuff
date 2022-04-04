
class conta_mae:
    estatico = 0
    def __init__(self,agencia):
        self._extrato = 100
        conta_mae.estatico+=1
        self.codigo_banco = "529"
        self.bloqueio = 0
        self._agencia = agencia
    
class conta_regional:
    cidade = "campinas"



class Conta(conta_mae,conta_regional):
    def __init__(self,titular,agencia):
        super().__init__(agencia)
        """cria objeto, titular nome do dono e extrato """
        self._titular = titular

    def gcidade(self):
        return self.cidade


    @property
    def gtitular(self):
        return self._titular
    @property
    def gagencia(self):
        return self._agencia
    
    @classmethod
    def ola(self,valor):
        self.count = valor
        return self.count

    @property #property deixa acessar o atributo como antes , o publico, metodo se escode como propriedade ?
    def extrato(self):
        return self._extrato
   
    @extrato.setter
    def extrato(self,value):
        print("setter")
        self._extrato = value

    @staticmethod
    def codigo():
        codigo = 10
        return codigo
    


    def _saque_ok(func):
        def innercheck(self,valor):

            if (self._extrato >= valor):
                return func(self,valor)
            else:
                print("Impossivel")
                return False
        
        return innercheck    
    
   
    @_saque_ok
    def saca(self,valor):
        self._extrato -= valor
        print("saque feito")
  
    def deposito(self,valor):
        self._extrato += valor


    def transfere(self,valor,conta_destino):
        self.saca(valor);
        conta_destino.deposito(valor);




def main():
    print(Conta.codigo())
    conta1 = Conta("Corto","222-222")
    conta2 = Conta("Case","333-333")
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
    print(conta1.gagencia)
    print(conta1.gtitular)
    print(conta2.estatico)
    print(conta1.gcidade())

if __name__ == '__main__':
    main()

