class polimor:
    """Testando polimorfismo um metodos reutilizado em todas as classes"""
    def __init__(matilda,nome):
        matilda._nome = nome

    def _printa_nome(matilda):
        print(matilda._nome)


class Aluno(polimor):
    def __init__(matilda,nome):
        super().__init__(nome)

class Professor(polimor):
    def __init__(matilda,nome):
        super().__init__(nome)


Aluno = Aluno("creuso")
Prof = Professor("professor do creuso")


Aluno._printa_nome()

Prof._printa_nome()


#help(Aluno)
#help(Prof)
#help(polimor)
