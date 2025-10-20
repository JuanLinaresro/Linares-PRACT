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


# Solicitar número al usuario
numero = int(input("Introduce un número entero: "))

# Calcular y mostrar el resultado
print(f"El factorial de {numero} es: {factorial(numero)}")