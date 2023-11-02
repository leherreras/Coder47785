class AbstractAuto:
    def andar(self):
        raise NotImplementedError

    def frenar(self):
        raise NotImplementedError


class Bus(AbstractAuto):
    def andar(self):
        return "estoy andando"

    def frenar(self):
        return "estoy frenando"
