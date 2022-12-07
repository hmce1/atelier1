X = int(input("Entrez le numéro X"))

def factorial(X):
    if X == 0 or X == 1: 
        return 1 #car factorielle de 0 ou 1 est égale à 1
    elif X > 1: 
        fact = 1
        for i in range(1,X+1):
                fact = (fact * i)
        return fact
    

print("X! = %d"%factorial(X))

