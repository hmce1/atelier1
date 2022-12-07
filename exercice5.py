n = int(input("Entrez le nombre n: "))

def somme(oneTOn):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum

print(somme(n))


