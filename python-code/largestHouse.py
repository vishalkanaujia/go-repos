'''
Assume that there is a lake with land. Assume number 0 represents water while positive numbers represent the land. The number represents the height of the land - so number 2 means the land is higher than number 1.

You mission, should you accept it, is to create a *square house* which has the largest area on that lake within the same land height.

Input : Two-dimensional array which represent the lake area.
Output: the biggest number represent the area of the house
'''

def findLargestSquareHouse(matrix, row, col):
    w, h = row, col
    maxSquare = [[0 for x in range(w)] for y in range(h)] 
    largest = 0
    
    for i in range(w):
        for j in range(h):
            if i == 0 or j == 0:
                maxSquare[i][j] = 1
            else:
                if (matrix[i][j] == matrix[i-1][j]) and \
                    (matrix[i][j] == matrix[i-1][j-1]) \
                        (matrix[i][j] == matrix[i][j-1]):
                            matrix[i][j] = min(min(maxSquare[i-1][j], maxSquare[i-1][j-1]), maxSquare[i][j-1]) + 1
                else:
                    maxSquare[i][j] = 1
            largest = max(largest, maxSquare[i][j])
            
    return largest*largest        
                