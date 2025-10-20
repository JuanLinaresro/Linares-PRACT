def promedio(lista):
    """
    Calcula el promedio (media) de una lista de números.
    """
    if len(lista) == 0:
        return "Error: la lista está vacía, no se puede calcular el promedio."
    
    suma = 0
    for numero in lista:
        suma += numero
    
    return suma / len(lista)


# Pedir al usuario los números
entrada = input("Introduce una lista de números separados por comas: ")

# Convertir la cadena en una lista de números
numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]

# Calcular y mostrar el promedio
print(f"El promedio de la lista es: {promedio(numeros)}")