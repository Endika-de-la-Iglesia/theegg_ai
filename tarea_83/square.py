def main():
    while True:
        x = input("Introduce un valor para el lado del cubo (debe ser un número entero): ")
        try:
            x = int(x)
            break
        except ValueError:
            print("No es un número entero.")
    area = square(x)
    print(area)

# Función que dé la superficie de un cuadrado conociendo el valor de un lado.
def square(x):
    area = x ** 2
    return area

if __name__ == "__main__":
    main()