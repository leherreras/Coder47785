class Animal(object):
    adn = True

    def __init__(self, cantidad_ojos: int, tipo_piel: str) -> None:
        self.cantidad_ojos = cantidad_ojos
        self.tipo_piel = tipo_piel

    def respirar(self) -> int:
        """
        Cantidad de veces que respira por minuto
        :return: int
        """
        return 30

    def correr(self) -> str:
        """
        me dice de que forma corre
        :return: str
        """
        return "correr normal"


class Mamifero:
    def respirar(self) -> str:
        return "estamos respirando por la nariz"


class Gato(Mamifero, Animal):
    def __init__(self, cantidad_ojos: int, tipo_piel: str, color: str, raza: str):
        Animal.__init__(self, cantidad_ojos=cantidad_ojos, tipo_piel=tipo_piel)
        self.color = color
        self.raza = raza

    def respirar(self) -> int:
        return Animal.respirar(self)


class Ballena(Animal):
    def correr(self) -> str:
        return "este animal no corre"

    def nadar(self) -> str:
        return "este animal nada lento"


def correr(x):
    return x.correr()


print(correr(Gato(cantidad_ojos=2, tipo_piel="peludo", color="rojo", raza="peludo")))

print(correr(Ballena(cantidad_ojos=2, tipo_piel="escamosa")))

print(correr(2))



# print(Animal.__mro__)
# print(Gato.__mro__)




# gato = Gato(cantidad_ojos=2, tipo_piel="peludo", color="rojo", raza="peludo")
# print(gato.respirar())
# print(gato.raza)
# print(gato.cantidad_ojos)
# print(gato.correr())
# print("--------------")
# ballena = Ballena(cantidad_ojos=2, tipo_piel="escamosa")
# print(ballena.cantidad_ojos)
# print(ballena.correr())
# print(ballena.nadar())
