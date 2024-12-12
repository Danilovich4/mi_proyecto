#Modulos de proyecto
#Un módulo es un archivo de Python que contiene definiciones de funciones, clases y variables que puedes importar y usar en otros archivos.

# utils/operaciones.py

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
