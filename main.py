"""
Crea una función llamada mensaje() que imprima "Hola, mundo".
Crea un decorador que modifique la función para que:
Imprima "Inicio de la función" antes de ejecutarse.
Imprima "Fin de la función" después de ejecutarse.
Aplica el decorador usando @decorar_funcion.
Ejecuta la función decorada y verifica el comportamiento.
"""
def decorador(funcion):
    def nueva_funcion ():
        print("Inicio de la funcion")
        funcion()
        print("Fin de la funcion")
    return nueva_funcion

@ decorador
def mensaje ():
    print("Hola mundo")

mensaje()
