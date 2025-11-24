class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 16):
        self.idade = idade
        self.nome = nome   
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'ola {id(self)}'
    
if __name__ == '__main__':
    Vito = Pessoa(nome = 'Vito')
    Pedro = Pessoa(Vito,nome = 'Pedro')
    print(Pessoa.cumprimentar)
    print(Pedro.cumprimentar())
    print(Pedro.nome)
    for filho in  Pedro.filhos:
        print(filho.nome)
    Pedro.sobrenome = 'de Castro'
    print(Pedro.__dict__)
    print(Vito.__dict__)
