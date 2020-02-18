class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)


pilaResultados = Pila()

def aCadena(n,base):
    cadenaConversion = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            pilaResultados.incluir(cadenaConversion[n])
        else:
            pilaResultados.incluir(cadenaConversion[n % base])
        n = n // base
    resultado = ""
    while not pilaResultados.estaVacia():
        resultado = resultado + str(pilaResultados.extraer())
    return resultado

print(aCadena(1453,16))
