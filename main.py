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
from utils.operaciones import multiplicar, dividir

def main():
    try:
        x = int(input("Introduce el primer número: "))
        y = int(input("Introduce el segundo número: "))
        # Realizamos las operaciones
        resultado_multiplicacion = multiplicar(x, y)
        resultado_division = dividir(x, y)
        # Mostramos los resultados
        print(f"Resultados:\nMultiplicación: {resultado_multiplicacion}\nDivisión: {resultado_division}")
    except ValueError:
        print("Error: Debes introducir números válidos.")

main()
