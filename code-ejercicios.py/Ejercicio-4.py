if __name__ == "__main__":
    pass  # Este archivo está diseñado para ser importado como módulo

def factorial(n):
    """
    Calcula el factorial de un número entero n usando un bucle for.
    """
    if n < 0:
        return "Error: el factorial no está definido para números negativos."
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


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


# Bloque principal de ejecución
if __name__ == "__main__":
    # Prueba de la función factorial
    numero = int(input("Introduce un número entero para calcular su factorial: "))
    print(f"El factorial de {numero} es: {factorial(numero)}")

    # Prueba de la función promedio
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
    print(f"El promedio de la lista es: {promedio(numeros)}")