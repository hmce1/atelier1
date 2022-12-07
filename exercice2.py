X = int(input("Entrez le numéro X"))

def factorial(X):
    fact = 1
    for i in range(1,X+1):
        fact = (fact * i)
    return fact

print("X! = %d"%factorial(X))

