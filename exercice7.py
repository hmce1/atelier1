s = input("Entrez la chaîne de caractères: ")
c = input("Entrez le caractère: ")

def fréquence(caractère):
    f = 0
    for i in s:
        if i == c:
            f += 1
    return f

print("La fréquence du caractère choisi dans la chaîne de caractères est: %s"%fréquence(c))

