def main():
    input_list = []
    while True:
        list_element = input("Inserte un número, cuando quiera parar de insertar números escriba STOP: ")
        if list_element.upper() == "STOP":
            break
        else:
            input_list.append(list_element)
    elements_sum = list_sum(input_list)
    print(elements_sum)
    return elements_sum


#Función que sume los valores de una lista
def list_sum(input_list):
    elements_sum = 0
    for element in input_list:
        try:
            element = float(element)
            elements_sum += element
        except ValueError:
            continue
    return elements_sum

if __name__ == "__main__":
    main()