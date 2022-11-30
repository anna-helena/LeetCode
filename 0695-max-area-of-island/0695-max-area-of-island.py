class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggest = 0
        seen = set()
        for i in range(len(grid)):
            print(grid[i])
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue
                if grid[i][j] == 0:
                    seen.add((i,j))
                    continue
                s = [(i,j)]
                curr_ar = 0
                seen.add((i,j))
                while s:
                    curr_i,curr_j = s.pop()
                    curr_ar += 1
                    #up
                    if curr_i > 0:
                        if (curr_i-1,curr_j) not in seen:
                            seen.add((curr_i-1,curr_j))
                            if grid[curr_i-1][curr_j] == 1:
                                s.append((curr_i-1,curr_j))
                    #down
                    if curr_i < len(grid)-1:
                        if (curr_i+1,curr_j) not in seen:
                            seen.add((curr_i+1,curr_j))
                            if grid[curr_i+1][curr_j] == 1:
                                s.append((curr_i+1,curr_j))
                    #left
                    if curr_j > 0:
                        if (curr_i,curr_j-1) not in seen:
                            seen.add((curr_i,curr_j-1))
                            if grid[curr_i][curr_j-1] == 1:
                                s.append((curr_i,curr_j-1))
                    #right
                    if curr_j < len(grid[0])-1:
                        if (curr_i,curr_j+1) not in seen:
                            seen.add((curr_i,curr_j+1))
                            if grid[curr_i][curr_j+1] == 1:
                                s.append((curr_i,curr_j+1))
                biggest = max(biggest,curr_ar)
        return biggest
                    
        