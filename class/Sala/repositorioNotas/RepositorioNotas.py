class RepositorioNotas:
    def __init__(self):
        self.__lista_alunos = []
        self.__media_sala = 0

    def add_aluno(self, aluno):
        self.__lista_alunos.append(aluno)


class Aluno:
    def __init__(self):
        self.__nome = ""
        self.__provas = []

    def addProva(self,prova):
        self.__provas.append(prova)


class Prova:
    def __init__(self, owner,name,tyype,grade):
        self.__name = name
        self.__type = tyype
        self.__grade = grade 
        self.__owner = owner

    def setGrade(self,grade):
        self.__grade = grade

    def printProva(self):
        print(self)


    def __str__(self):
        print(("{} {} {} {}").format(self.__grade,self.__name,self.__type,self.__owner))

    def __repr__(self):
        print(Prova())
        
