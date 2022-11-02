class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i,row in enumerate(board):
            prev = set()
            for nr in row:
                print(prev)
                if nr == ".":
                    continue
                if nr in prev:
                    return False
                prev.add(nr)
        for i in range(9):
            prev = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in prev:
                    return False
                prev.add(board[j][i])
        for i in range(3):
            for j in range(3):
                prev = set()
                for i_ in range(3):
                    for j_ in range(3):
                        if board[i*3+i_][j*3+j_] == ".":
                            continue
                        if board[i*3+i_][j*3+j_] in prev:
                            return False
                        prev.add(board[i*3+i_][j*3+j_])
        return True
                        
        
        