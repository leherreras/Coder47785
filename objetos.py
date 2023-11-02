class Persona:
    pass
# _ protegido #
# __ privado -
# publico +


class Dog(object):
    tipo = "mamifero"
    _cantidad_ojos = 2

    def __init__(self, raza: str, color: str, duenio: Persona) -> None:
        self.__raza = raza
        self.color = color
        self.cantidad_patas = 4
        self.duenio = duenio

    def __str__(self):
        return f"Yo soy un perro de raza {self.__raza} y de color {self.color}"

    def __iter__(self):
        for ra in self.__raza:
            yield ra

    def __len__(self):
        return len(self.__raza)

    def _ladrar(self) -> str:
        if self.__raza == "doberman":
            return "gggggggggggggg"
        return "wofff"

    def caminar(self, cantida_pasos):
        if cantida_pasos > 100:
            return "ha camindao mucho"
        return "ha camindao poco"


per = Persona()
dog_1 = Dog(raza="doberman", color="Negro", duenio=per)
# print(dog_1._cantidad_ojos)
print(dog_1)
print(dog_1.__raza)
print(dog_1.color)
print(dog_1._ladrar())
print(dog_1.caminar(500))
print(len(dog_1))

for val in dog_1:
    print(val)
print("------------------------")
#
# dog_2 = Dog(raza="pastor aleman", color="negro")
# print(dog_2.raza)
# print(dog_2.color)
# print(dog_2.ladrar())
