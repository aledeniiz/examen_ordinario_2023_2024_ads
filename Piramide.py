def crear_piramide(n_pisos):
    if n_pisos < 1:
        print("El número de pisos debe ser mayor o igual a 1.")
        return

    for i in range(1, n_pisos + 1):
        espacios = n_pisos - i
        print(" " * espacios + "*" * (2 * i - 1) + " " * espacios)

def main():
    try:
        n_pisos = int(input("Ingrese el número de pisos para la pirámide: "))
        
        if n_pisos < 1:
            print("El número de pisos debe ser mayor o igual a 1.")
            return

        crear_piramide(n_pisos)

    except ValueError:
        print("Error: Ingrese un número entero válido.")

if __name__ == "__main__":
    main()