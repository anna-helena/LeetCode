class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #move from right to left from button to up
        count = 0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                #print(matrix)
                if matrix[i][j] == 0:
                    continue
                if (j < (len(matrix[0])-1)) & (i < (len(matrix)-1)):
                    matrix[i][j] = min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]) + 1
                    count += matrix[i][j]
                else:
                    count += 1
        return count