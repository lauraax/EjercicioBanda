class Instrumento:
     def afinar(self):
         pass
     def tocar(self):
         pass
     def mostrar(self):
         return "instrumento: " + str(type(self)).split(".")[-1][:-2]
    
class Guitarra(Instrumento):
    def afinar(self):
        return 'Afinando guitarra'

    def tocar(self):
        return 'Tocando guitarra'
        
class Saxo(Instrumento):
    def afinar(self):
        return 'Afinando saxofón'

    def tocar(self):
        return 'Tocando saxofón'
    
class Tiple(Instrumento):
    def afinar(self):
        return 'Afinando tiple'

    def tocar(self):
        return 'Tocando tiple'

class Piano(Instrumento):
    def afinar(self):
        return 'Afinando piano'

    def tocar(self):
        return 'Tocando piano'

class Bongos(Instrumento):
    def afinar(self):
        return 'Afinando bongos'

    def tocar(self):
        return 'Tocando bongos'
    
class Maracas(Instrumento):
    def afinar(self):
        return 'Afinando maracas'

    def tocar(self):
        return 'Tocando maracas'

class Trompeta(Instrumento):
    def afinar(self):
        return 'Afinando trompeta'

    def tocar(self):
        return 'Tocando trompeta'

class Violin(Instrumento):
    def afinar(self):
        return 'Afinando violin'

    def tocar(self):
        return 'Tocando violin'

    