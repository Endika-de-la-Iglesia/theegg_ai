def main():
    list_one, list_two = get_lists()
    similarities, list_equal_values = list_comparison(list_one, list_two)
    if similarities:
        print(f"Hay valores coincidentes: {list_equal_values}")
    else:
        print("No hay valores coincidentes")
    

def get_lists():
    list_one = []
    list_two = []
    while True:
        element_list_one = input("Introduce elementos para la primera lista, escribe STOP para finalizar: ")
        if element_list_one.upper() == "STOP":
            break
        else:
            list_one.append(element_list_one)

    while True:
        element_list_two = input("Introduce elementos para la segunda lista, escribe STOP para finalizar: ")
        if element_list_two.upper() == "STOP":
            break
        else:
            list_two.append(element_list_two)
    return list_one, list_two
            
#Función que compare dos listas y encuentre si hay algún valor coincidente
def list_comparison(list_one, list_two):
    list_equal_values = []
    for element in list_one:
        if element in list_two:
            list_equal_values.append(element)
    if len(list_equal_values) == 0:
        similarities = False
    else:
        similarities = True

    return similarities, list_equal_values

if __name__ == "__main__":
    main()