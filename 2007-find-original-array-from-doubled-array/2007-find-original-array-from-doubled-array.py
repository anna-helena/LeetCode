from sortedcontainers import SortedDict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        sorted_ = SortedDict()
        for val in changed:
            temp = sorted_.get(val,0)
            temp += 1
            sorted_[val] = temp
        solution = []
        if 0 in sorted_:
            if sorted_[0]%2 != 0:
                return []
            for i in range(sorted_[0]//2):
                solution.append(0)
            del sorted_[0]
        while sorted_:
            key,val = sorted_.peekitem(0)
            if key*2 in sorted_:
                if sorted_[key*2] >= val:
                    for i in range(val):
                        solution.append(key)
                    del sorted_[key]
                    temp = sorted_[key*2] - val
                    if temp == 0:
                        del sorted_[key*2]
                    else:
                        sorted_[key*2] = temp
                else:
                    return []
            else:
                return []
        return solution
                
        
            
        
    