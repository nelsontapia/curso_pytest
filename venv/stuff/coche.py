# class coche

class Car:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print('El', self.marca, self.modelo, 'ha arrancado')