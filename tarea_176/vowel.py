def main():
    while True:
        character = input("Introduce un carácter : ")
        if len(character) == 1:
            break
    vowel_yes = vowel_id(character)
    if vowel_yes:
        print("Es una vocal")
    else:
        print("No es una vocal")

#Función que determine si un carácter previamente dado es vocal o no
def vowel_id(character):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_yes = False
    if character in vowels:
        vowel_yes = True
    return vowel_yes

if __name__ == "__main__":
    main()