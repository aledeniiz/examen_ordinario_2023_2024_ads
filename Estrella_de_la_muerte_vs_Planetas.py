class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion


class Concordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, 1)


class Ilum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, 2)


class Kamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, 3)


class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.puntos_de_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_de_vida -= planeta.volumen
        else:
            print(f"La Estrella de la Muerte no puede destruir el planeta {planeta.nombre}.")


# Crear instancias de las clases de planetas
concordia = Concordia()
ilum = Ilum()
kamino = Kamino()

# Crear instancia de la Estrella de la Muerte
estrella_muerte = EstrellaDeLaMuerte()

# Llamar al método destruir_planeta para cada planeta
estrella_muerte.destruir_planeta(concordia)
estrella_muerte.destruir_planeta(ilum)
estrella_muerte.destruir_planeta(kamino)