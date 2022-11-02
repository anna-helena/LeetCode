from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for strs_ in strs:
            letters = [0]*26
            for s_ in strs_:
                letters[ord(s_)-ord('a')] += 1
            sol[tuple(letters)].append(strs_)
        return sol.values()
            
        
        