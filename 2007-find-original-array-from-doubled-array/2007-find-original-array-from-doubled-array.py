from collections import defaultdict
from sortedcontainers import SortedDict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        #double missing
        #[1:2 3:6 4:8 6: 8:]
        #half missing
        #[4:2 ]
        '''
        1:1,2:1,3:1,4:1,5:1,6:1,8:1
        [1:2,3:6,4:8,2:4,6:,8:]
        
        [4:2,6:3,8:4,2:1]
        2:2
        4:2
        6:1
        3:1
        8:1
        (4,2) -> 2
        (6,3) -> 1
        (8,4) -> 1.5
        (2,1) -> 1.5
        4,2
        '''
        #build two prevs keys to have all possible combination
        #find set of best combis with adapted DFS
        #go one by one remember combi as set stop when nr reached, if not ,remove when old one gets two hits (but hits are reduced if one new hits two....)
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
                
        
            
        
    