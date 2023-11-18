def main():
    sentence = get_sentence()
    print(sentence_lenght(sentence))

def get_sentence():
    sentence = input("Introduce una frase: ")
    return sentence

#Función que diga la longitud de una frase
def sentence_lenght(sentence):
    ch = 0
    for character in sentence:
        ch += 1
    return ch

if __name__ == "__main__":
    main()