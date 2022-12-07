n = int(input("Entrez le nombre n: "))

def somme(OnetoN):
    sum = 0
    for i in range ( 1, n+1):
        sum += i
    return sum

print(somme(n))


