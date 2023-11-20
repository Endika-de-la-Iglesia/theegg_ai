def main():
    planet, time = get_segundos_caida()
    if planet == "Tierra":
        h = tierra(time)
    elif planet == "Marte":
        h= marte(time)
    elif planet == "Jupiter":
        h = jupiter(time)

    print(f'La altura del objeto en el planeta {planet} es {h} m')


#Obtener el parámetro de interés
def get_segundos_caida():

    list_planets = ["Tierra", "Marte", "Jupiter"]

    while True:
        try:
            planet = input("Introduzca el nombre del planeta: ").strip().capitalize()
            if planet in list_planets:
                break
            else:
                raise ValueError
        except ValueError:
            print("Introduzca el nombre de uno de estos planetas: Tierra, Marte, Jupiter")

    while True:
        try:
            time = float(input("Tiempo de caída en segundos: "))
            if time >= 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("No ha introducido un número válido.")

    return planet, time

# Función para calcular la altura a la que está un objeto en el planeta Tierra
def tierra(time):
    g = 9.8
    h = 0.5 * g * time ** 2
    return h

def marte(time):
    g = 3.7
    h = 0.5 * g * time ** 2
    return h

def jupiter(time):
    g = 24.8
    h = 0.5 * g * time ** 2
    return h

#Para testear las funciones
if __name__ == "__main__":
    main()
