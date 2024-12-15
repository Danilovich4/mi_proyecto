"""
Crea una función llamada mensaje() que imprima "Hola, mundo".
Crea un decorador que modifique la función para que:
Imprima "Inicio de la función" antes de ejecutarse.
Imprima "Fin de la función" después de ejecutarse.
Aplica el decorador usando @decorar_funcion.
Ejecuta la función decorada y verifica el comportamiento.
"""
def decorador(funcion):
    def nueva_funcion (*arg, **kwarg):
        print("Inicio de la funcion")
        result = funcion(*arg, **kwarg)
        print("Fin de la funcion")
        return result
    return nueva_funcion

@ decorador
def sumar (a, b):
    sum = a + b
    print(f"La suma es: {sum}")

sumar(5,3)
