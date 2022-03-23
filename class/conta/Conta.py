class Conta:
    def __init__(self,titular):
        self.__titular = titular
        self.__extrato = 100

    def extrato(self):
        print("Saldo eh R$ {}".format(self.__extrato))


    def deposito(self,valor):
        self.__extrato += valor

    def saca(self,valor):
        self.__extrato -= valor


conta1 = Conta("joao")

conta1.extrato()
conta1.deposito(10)
conta1.extrato()
conta1.saca(50)
conta1.extrato()

