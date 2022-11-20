from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        ones = {}
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    ones[(x,y)] = 1
        count = 0
        for one in ones:
            if ones[one] == 0:
                continue
            s = []
            s.append(one)
            ones[one] = 0
            count += 1
            while s:
                x,y = s.pop()
                #up
                if x > 0:
                    temp = grid[x-1][y]
                    if temp == '1':
                        if ones[(x-1,y)] == 1:
                            ones[(x-1,y)] = 0
                            s.append((x-1,y))
                #down
                if x < len(grid)-1:
                    temp = grid[x+1][y]
                    if temp == '1':
                        if ones[(x+1,y)] == 1:
                            ones[(x+1,y)] = 0
                            s.append((x+1,y))
                #left
                if y > 0:
                    temp = grid[x][y-1]
                    if temp == '1':
                        if ones[(x,y-1)] == 1:
                            ones[(x,y-1)] = 0
                            s.append((x,y-1))
                #right
                if y < len(grid[0])-1:
                    temp = grid[x][y+1]
                    if temp == '1':
                        if ones[(x,y+1)] == 1:
                            ones[(x,y+1)] = 0
                            s.append((x,y+1))
        return count
                
            