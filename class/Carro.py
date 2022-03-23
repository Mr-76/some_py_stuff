class Carro:
    
    LOCAL_PRODUCAO = "BRAZIL" #static -- todas as instancias da classe tem
                                # pode mudar com Carro.LOCAL_PRODUÇAO = NOVOLOCAL


    def __init__(self,marca,ano,cor,marchas,modelo):
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__marchas = marchas
        self.__modelo = modelo
    
    def GetValores(self):
        return print("{}\n{}\n{}\n{}\n{}".format(self.__marca,self.__ano,self.__modelo,self.__marchas,self.__ano))


HB20 = Carro("Hyundai",2020,"Branco",6,"sport")

HB20.GetValores()

