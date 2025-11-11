# 1 Crear un Personaje

class Personaje:
    poder_global = 100  # Atributo de clase
    def __init__(self, fuerza, nombre, raza, vida):
        self.fuerza = fuerza  # Atributo de instancia
        self.nombre = nombre
        self.raza = raza
        self.vida = vida
        
# Funcionalidades o comportamientos del personaje
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un {self.raza}")
        print(f"Tengo {self.vida} puntos de vida y {self.fuerza} de fuerza.")
        print(f"Mi poder global es {self.poder_global}")
        print("")
        print("")
        print("")
        
    
    # Método para atacar a otro personaje
    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            print(f"{otro_personaje.nombre} ya está derrotado.")
            return
        daño = self.fuerza
        otro_personaje.vida -= daño
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y le quita {daño} puntos de vida.")
        if otro_personaje.vida <= 0:
            otro_personaje.vida = 0
            print(f"{otro_personaje.nombre} ha sido derrotado.")
        else:
            print(f"A {otro_personaje.nombre} le quedan {otro_personaje.vida} puntos de vida.")
            if otro_personaje.vida <= 20:
                otro_personaje.curarse(10)
                print(f"{otro_personaje.nombre} se ha curado 10 puntos de vida.")
                otro_personaje.mostrar_estado()
                otro_personaje.comparar_fuerza(p1)
                otro_personaje.comparar_fuerza(p2)
                otro_personaje.comparar_fuerza(p3)

    # Método para curarse
    def curarse(self, cantidad):
        self.vida += cantidad
        print(f"{self.nombre} se cura {cantidad} puntos de vida. Vida actual: {self.vida}")
    # Método para mostrar el estado del personaje
    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Vida: {self.vida}, Fuerza: {self.fuerza}")
    # Método de clase para mostrar el poder global
    @classmethod
    def mostrar_poder_global(cls):
        print(f"Poder global: {cls.poder_global}")
    # Método estático para mostrar un mensaje de bienvenida
    @staticmethod
    def mensaje_bienvenida():
        print("Bienvenido al juego de personajes.")
    # Método para comparar la fuerza de dos personajes
    def comparar_fuerza(self, otro_personaje):
        if self.fuerza > otro_personaje.fuerza:
            print(f"{self.nombre} es más fuerte que {otro_personaje.nombre}.")
        elif self.fuerza < otro_personaje.fuerza:
            print(f"{otro_personaje.nombre} es más fuerte que {self.nombre}.")
        else:
            print(f"{self.nombre} y {otro_personaje.nombre} tienen la misma fuerza.")
# Ejemplo de uso
Personaje.mensaje_bienvenida()
Personaje.mostrar_poder_global()

p1 = Personaje(50, "Aragorn", "Humano", 100)
p2 = Personaje(70, "Legolas", "Elfo", 90)
p3 = Personaje(60, "Gimli", "Enano", 110)
p1.presentarse()
p2.presentarse()
p3.presentarse()

p1.atacar(p2)
p2.atacar(p3)
p3.atacar(p1)
p1.atacar(p3)
p2.atacar(p1)
p3.atacar(p2)
p1.atacar(p2)
p2.atacar(p3)
p3.atacar(p1)

p1.mostrar_estado()
p2.mostrar_estado()
p3.mostrar_estado()

p1.comparar_fuerza(p2)
p2.comparar_fuerza(p3)
p3.comparar_fuerza(p1)