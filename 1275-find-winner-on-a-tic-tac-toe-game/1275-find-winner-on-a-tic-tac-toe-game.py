class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """

        winning = [0]*16
        for i,move in enumerate(moves):
            max_cont = 0
            row, col = move
            #for row
            idx = row + 8*(i%2)
            winning[idx] += 1
            max_cont = max(max_cont,winning[idx])
            #for col
            idx = col + 3 + 8*(i%2)
            winning[idx] += 1
            max_cont = max(max_cont,winning[idx])
            #for diag
            if(row == col):
                idx = 6 + 8*(i%2)
                winning[idx] += 1
                max_cont = max(max_cont,winning[idx])
            if(move in [[2,0],[1,1],[0,2]]):
                idx = 7 + 8*(i%2)
                winning[idx] += 1
                max_cont = max(max_cont,winning[idx])
            if max_cont == 3:
                if (i%2):
                    return "B"
                return "A"
        if len(moves) == 9:
            return "Draw"
        return "Pending"
        