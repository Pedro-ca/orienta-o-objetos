class Pessoa:
    def __init__(self, nome = None, idade = int):
        self.nome = nome   

    def cumprimentar(self):
        return f'ola {id(self)}'
    
if __name__ == '__main__':
    p = Pessoa('Pedro')
    print(Pessoa.cumprimentar)
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Victor'
    print(p.nome)
