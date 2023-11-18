import re

def main():
    number_one, number_two, number_three = get_numbers()
    print(highest_number(number_one, number_two, number_three))

#Pedir los números
def get_numbers():
    while True:
        try:
            numbers = input("Introduzca tres números separados por '_': ").strip()
            #Patrón regex para buscar tres números separados por '_', pueden ser tanto int como floats
            pattern = re.compile(r'(\d+(?:\.\d+)?)_(\d+(?:\.\d+)?)_(\d+(?:\.\d+)?)')
            match = pattern.match(numbers)
            if match:
                number_one = float(match.group(1))
                number_two = float(match.group(2))
                number_three = float(match.group(3))
                break
            else:
                raise ValueError("Fallo en el formato")
        except ValueError:
            print("Por favor, introduzca tres números en el formato requerido.")
    return number_one, number_two, number_three

# Función que diga el máximo de 3 números dados
def highest_number(number_one, number_two, number_three):
    if (number_one > number_two and number_one > number_three) or (number_one == number_two > number_three) or (number_one == number_three > number_two):
        return number_one
    elif (number_two > number_one and number_two > number_three) or (number_two == number_three > number_one):
        return number_two
    elif number_three > number_one and number_three > number_two:
        return number_three
    else:
        message_equal = f"Todos los números son iguales, así que no hay ninguno más alto que {number_one}."
        return message_equal
    
if __name__ == "__main__":
    main()
