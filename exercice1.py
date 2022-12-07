
X = int(input("Entrez le numéro X"))
n = int(input("Entrez la puissance n"))

def puissanceXn(X,n):
    power = 1
    for i in range(1,X+1):
            power = power * X
    return power
            
print("X^n est égale à: %d"%puissanceXn(X,n))         

    
    


    

