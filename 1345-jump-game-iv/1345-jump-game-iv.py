from collections import deque
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        seen = set()
        prev = {}
        prev[0] = None
        same = defaultdict(list)
        for idx,val in enumerate(arr):
            same[val].append(idx)
            
        q = deque()
        q.append((0,0))
        seen.add(0)
        result = 0
        while(q):
            curr_idx, dist = q.popleft()
            print(curr_idx, dist)
            if curr_idx == len(arr)-1:
                break        
            #add left
            if (curr_idx > 0):
                l_idx = curr_idx - 1
                if (l_idx not in seen):
                    q.append((l_idx,dist+1))
                    prev[l_idx] = curr_idx
                    seen.add(l_idx)
            #add right
            if (curr_idx < len(arr)-1):
                r_idx = curr_idx + 1
                if (r_idx not in seen):
                    q.append((r_idx,dist+1))
                    prev[r_idx] = curr_idx
                    seen.add(r_idx)
            #add same number
            #for new_idx in same[arr[curr_idx]]:
            temp_arr = same[arr[curr_idx]]
            for i in range(len(temp_arr)-1,-1,-1):
                new_idx = temp_arr[i]
                if new_idx == curr_idx:
                    continue
                if (new_idx not in seen):
                    q.append((new_idx,dist+1))
                    prev[new_idx] = curr_idx
                    seen.add(new_idx)
                if new_idx == (len(arr)-1):
                    return (dist + 1)
            del same[arr[curr_idx]]
        before = prev[curr_idx]
        while before is not None:
            result += 1
            before = prev[before]
        return dist