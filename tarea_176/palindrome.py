def main():
    word = input("Introduzca una palabra: ").strip()
    palindrome = is_palindrome(word)
    if palindrome:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

#Función que diga si una palabra dada es un palíndromo
def is_palindrome(word):
    palindrome = False
    index = -1
    word_lenght = 0
    for ch in word:
        if ch == word[index]:
            index -= 1
            word_lenght += 1
    if word_lenght == len(word):
        palindrome = True
    return palindrome

if __name__ == "__main__":
    main()