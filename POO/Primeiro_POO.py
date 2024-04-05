class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plin plin')

    def parar(self):
        print('Parando')

    def correr(self):
        print('Vruum...')

b1 = Bicicleta('vermelha','caloi',2022,600)