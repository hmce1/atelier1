string = input("Entrez la chaîne de caractères: ")
character = input("Entrez le caractère: ")

def fréquence(string,character):
    f = 0
    for i in string:
        if i == character:
            f += 1
    return f

print("La fréquence du caractère choisi dans la chaîne de caractères est: %s"%fréquence(string,character))

