class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #move from right to left from button to up
        count = 0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                #print(matrix)
                if matrix[i][j] == 0:
                    continue
                count += 1
                if (j < (len(matrix[0])-1)) & (i < (len(matrix)-1)):
                    min_val = min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
                    count += min_val
                    matrix[i][j] = min_val + 1
        return count