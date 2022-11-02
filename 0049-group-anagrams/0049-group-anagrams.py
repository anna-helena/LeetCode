from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        prev_dict = []
        sol = []
        translate = {}
        for strs_ in strs:
            new_dict = defaultdict(int)
            for s in strs_:
                new_dict[s] += 1
            found = False
            for idx,prev_ in enumerate(prev_dict):
                if prev_ == new_dict:
                    found = True
                    temp = sol[translate[idx]]
                    temp.append(strs_)
                    sol[translate[idx]] = temp
                    break
            if not found:
                translate[len(prev_dict)] = len(sol) 
                sol.append([strs_])
                prev_dict.append(new_dict)
        return sol
            
        
        