from exercice2 import factorial #nous sommes dans le même dossier

n = 5

def sum(n):
    somme = 0
    for i in range(1,n+1):
        somme += factorial(i)/i
    return somme

print("La somme de 1!/1 + 2!/2 + 3!/3 + 4!/4 + 5!/5 égale à %d"%sum(n))
