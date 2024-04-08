class Passaro:
    def voar(self):
        print("Voando...")

# Herança: Filho de Pássaro(Pardal)
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()

p1 = Pardal
p2 = Avestruz

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())