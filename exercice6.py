n = int(input("Entrez le nombre choisi: "))

def compter(n):
    if n == 0:
        return 1
    sum = 0
    while n!=0:
        n = n//10 # on va diviser le nombre choisi sur 10 jusqu'à le quotient devient 0
        sum += 1
    return sum

print("Le nombre des chiffres du nombre choisi est: %d"%compter(n))