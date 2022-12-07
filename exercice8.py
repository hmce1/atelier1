def ShowElement(Matrix, Element):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == Element:
                return "La poisition de l'élément %d est [%d][%d]"%(Element,i,j)
    return "L'élément %d n'esxite pas dans cette matrice"%(Element)

        
matrix = [[1,2,3],[4,5,6],[7,8,9]] 

print(ShowElement(matrix, 9))


