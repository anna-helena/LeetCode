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
        q.append(0)
        seen.add(0)
        result = 0
        while(q):
            curr_idx = q.popleft()
            if curr_idx == len(arr)-1:
                break        
            #add left
            if (curr_idx > 0):
                l_idx = curr_idx - 1
                if (l_idx not in seen):
                    q.append(l_idx)
                    prev[l_idx] = curr_idx
                    seen.add(l_idx)
            #add right
            if (curr_idx < len(arr)-1):
                r_idx = curr_idx + 1
                if (r_idx not in seen):
                    q.append(r_idx)
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
                    q.append(new_idx)
                    prev[new_idx] = curr_idx
                    seen.add(new_idx)
                if new_idx == (len(arr)-1):
                    break
            del same[arr[curr_idx]]
        before = prev[curr_idx]
        while before is not None:
            result += 1
            before = prev[before]
        return result