Nombres_de_perros = []

def agregar(nombre):
    Nombres_de_perros.append(nombre)

def mostrar():
    return Nombres_de_perros

def editar(posicion, nuevo_nombre):
    Nombres_de_perros[posicion] = nuevo_nombre

def sacar(posicion):
    return Nombres_de_perros.pop(posicion)

def eliminar(nombre):
    Nombres_de_perros.remove(nombre)

agregar("jose")
agregar("doki")
agregar("firulais")

editar(0, "wismichu")
agregar("roro")

print(sacar(0))
eliminar("doki")
print(mostrar())