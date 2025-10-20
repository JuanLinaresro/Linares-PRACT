def tabla_multiplicar():
    try:
        numero = int(input("Introduce un número: "))
        if numero > 0:
            print(f"\nTabla de multiplicar del {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Este bloque asegura que el código solo se ejecute
# si el archivo se ejecuta directamente (no cuando se importa como módulo)
if __name__ == "__main__":
    tabla_multiplicar()
    