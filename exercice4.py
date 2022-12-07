Decimal = 987 #c'est la fonction dans le cas où Decimal est positif

def ConvertBinToDic(Decimal):
    Binary = "" #on a définit binary comme une chaîne de caractères vide
    while Decimal >= 0:
        Binary += str(Decimal % 2) #append permet d'ajouter decimal % 2 dans Binary
        Decimal = Decimal // 2 #on va diviser sur 2 et obtient le quotient jusqu'à 0
        if Decimal == 0:
            break
    return Binary[::-1] #on a  slicing: [start: end: step] inverser la chaîne de caractères

print(ConvertBinToDic(Decimal))



