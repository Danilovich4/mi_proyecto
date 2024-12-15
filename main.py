"""
Crea un módulo llamado operaciones.py con las siguientes funciones:
multiplicar(a, b)
dividir(a, b) (maneja la división por cero).
Organiza tu proyecto con la siguiente estructura:
css
Copiar código
mi_proyecto/
    main.py
    utils/
        __init__.py
        operaciones.py
Importa y usa las funciones de operaciones.py en main.py para:
Multiplicar dos números ingresados por el usuario.
Dividir dos números ingresados por el usuario.
"""

# Solicitar números al usuario con manejo de errores
def sol_num():
    try:
        a = int(input("Introduce un número a: "))
        b = int(input("Introduce un número b: "))
        return a, b
    except ValueError:
        print("Error: Debes introducir un número válido.")
        return None

# Realizar operaciones matemáticas
def operaciones(a, b):
    try:
        suma = a + b
        resta = a - b
        multi = a * b
        div = a / b
        print(f"Resultados:\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Función principal
def main():
    numeros = sol_num()
    if numeros:  # Verifica si `sol_num()` devolvió una tupla válida
        a, b = numeros
        operaciones(a, b)
        print (numeros)

main()