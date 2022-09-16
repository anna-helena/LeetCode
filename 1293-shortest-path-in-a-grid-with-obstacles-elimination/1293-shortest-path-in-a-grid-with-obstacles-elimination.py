from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque()
        seen = {}

        y = len(grid) - 1
        x = len(grid[0]) - 1
        seen[(x,y)] = k
        steps = 0
        q.append((x,y,k,0))
        
        while(q):
            #print(q)
            x_,y_,k_,steps = q.popleft()
            #print(x_,y_,k_,steps)
            if((x_ == 0) & (y_ == 0)):
                return steps
            #left
            if x_ > 0:
                x = x_ - 1
                y = y_
                    
                if (((x,y) not in seen) or (seen[(x,y)] < k_)) :
                    temp = grid[y][x]
                    if ((temp == 1) & (k_ > 0)):
                        q.append((x,y,k_-1,steps+1))
                        seen[(x,y)] = k_
                    elif(temp == 0):
                        q.append((x,y,k_,steps+1))
                        seen[(x,y)] = k_

                    
            #up
            if y_ > 0:
                x = x_
                y = y_ - 1
                
                if (((x,y) not in seen) or (seen[(x,y)] < k_)) :
                    temp = grid[y][x]
                    if ((temp == 1) & (k_ > 0)):
                        q.append((x,y,k_-1,steps+1))
                        seen[(x,y)] = k_
                    elif(temp == 0):
                        q.append((x,y,k_,steps+1))
                        seen[(x,y)] = k_
            #right
            if x_ < len(grid[0]) -1:
                x = x_ + 1
                y = y_
     
                if (((x,y) not in seen) or (seen[(x,y)] < k_)) :
                    temp = grid[y][x]
                    if ((temp == 1) & (k_ > 0)):
                        q.append((x,y,k_-1,steps+1))
                        seen[(x,y)] = k_
                    elif(temp == 0):
                        q.append((x,y,k_,steps+1))
                        seen[(x,y)] = k_
            #down
            if y_ < len(grid) -1:
                x = x_ 
                y = y_ + 1
              
                if (((x,y) not in seen) or (seen[(x,y)] < k_)) :
                    temp = grid[y][x]
                    if ((temp == 1) & (k_ > 0)):
                        q.append((x,y,k_-1,steps+1))
                        seen[(x,y)] = k_
                    elif(temp == 0):
                        q.append((x,y,k_,steps+1))
                        seen[(x,y)] = k_
        return -1
                