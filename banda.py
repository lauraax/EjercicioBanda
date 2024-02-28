from musicos import *
from random import choice, randint

class Banda:
    def __init__(self):
        self.musicos = []
        self.instrumentos = [Guitarra(), Saxo(), Tiple(), Piano(), Bongos(), Maracas(), Trompeta(), Violin()]
        self.amigos = ["Hugo", "Juan", "Miguel", "Maria", "Ana", "Juana", "Pedro"]
    
    def crear_banda(self, cantidad_musicos):
        for i in range (cantidad_musicos):
            self.musicos.append(Musico(choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(choice(self.instrumentos))

    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())
    
    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())
    
    def mostrar_banda(self):
        for m in self.musicos:
            print("\n Musico: ",m.nombre)
            print(m.instrumento.mostrar())
            
if __name__ == '__main__':
    b = Banda()
    num= randint(1,8)
    b.crear_banda(num)
  
    print("\t***BANDA***")
    print("Número musicos en la banda: ",num)
    b.mostrar_banda()
    print("\nAfinamos la banda: ")
    b.afinar_banda()
    print('\nA tocar: ')
    b.tocar_banda()
