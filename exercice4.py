Decimal = 987

def ConvertBinToDic(Decimal):
    Binary = [] #on a définit binary comme une liste vide
    while Decimal >= 0:
        Binary.append(Decimal % 2) #append permet d'ajouter decimal % 2 dans la liste binary
        Decimal = Decimal // 2 #on va diviser sur 2 et obtient le quotient jusqu'à 0
        if Decimal == 0:
            break
    Binary.reverse() #reserve est une méthode permet de inverser les objets de la liste Binary
    return Binary

print(ConvertBinToDic(Decimal))



