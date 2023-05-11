class Person():
    def __init__(self, nome, idade, id):
        self.nome = nome
        self.idade = idade
        self.id = id

    def fazAniversario(self):
        self.idade = self.idade + 1