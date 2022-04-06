class InfoPessoa:
    def __init__(chapolin,cpf,nome):
        chapolin._cpf = cpf
        chapolin._nome = nome




class NotaFiscal(InfoPessoa):
    def __init__(chapolin,cpf,nome,valor,cnpj_loja,itens):
        super().__init__(nome,cpf)
        chapolin.itens = itens
        chapolin._valor = valor
        chapolin._cnpj_loja = cnpj_loja
        chapolin._itens = itens


    def __str__(chapolin):
        frase = "classe sobre criaçao de uma nota eletronica"
        return frase



    @property
    def _imprime_nota(chapolin):
        print("Nota Fiscal eletronica")
        print("Valor pago : {}".format(chapolin._valor))
        print("pelo cpf de numero {} e nome {}".format(chapolin._cpf,chapolin._nome))
        print("Recebido para o cnpj {}".format(chapolin._cnpj_loja))
        for i in chapolin._itens:
            print(i)
itens = ["cadeira rgb","mouse rgb","monitor rgb"]
nota_gamer = NotaFiscal("000.000.000-00","pirata alma negra",10000,"00.000.000/0000-00",itens)

nota_gamer._imprime_nota
print(nota_gamer)
