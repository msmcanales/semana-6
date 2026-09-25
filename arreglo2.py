"""
Create
read 
update
delete
Registrar un listado de edades.

"""

edades = []

def agregaredad(edad):
    edades.append(edad)

def mostrar_edades():
    return edades 

def actualizar_edad(index,edad):
    edades [index] = edad

def eliminar_edad(edad):
    edades.remove(edad)

def menu():
    print (""" 
0. Salir 
1. Agregar edad
2. Editar edades
3. Actualizar edad
4. Eliminar edad

    """)
    op = int(input())
    return op 


def pedir_dato():
    dato =0
    while True: 
       try:
           dato = int(input(""))
           return dato 
       except.ValueError:
            print("Ingrese un valor valido")




def seleccionar_opcion():
    op = menu()
    if op == 1:
        print("Ingrese la edad a agregar: ")
        edad = pedir_dato()
        agregaredad(edad)
    elif op == 2:
        print("Dime en que posicion se encuentra")
        pos = pedir_dato()
        print("dime la nueva edad")
        edad = pedir_dato()
        actualizar_edad(pos, edad)
    elif op == 3:
        print("Ingrese la edad a eliminar: ")
        edad = pedir_dato()
        eliminar_edad(edad)
    elif op == 4:
     print (mostrar_edades())
    elif op == 0:
      print("Adios")
      return 0

    else:
        print("Opcion no valida")
    seleccionar_opcion()

def main():
    seleccionar_opcion()

main()


