class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggest = 0
        seen = set()
        for i in range(len(grid)):
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
                    for new_i,new_j in ((curr_i-1,curr_j),(curr_i+1,curr_j),(curr_i,curr_j-1),(curr_i,curr_j+1)):
                        if (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i,new_j) not in seen):
                            seen.add((new_i,new_j))
                            if grid[new_i][new_j]:
                                s.append((new_i,new_j))
                biggest = max(biggest,curr_ar)
        return biggest
                    
        