from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #at each step check what is the maximum 
        occurences = defaultdict(int)
        heap = []
        i = 0
        max_len = 0
        for j,s_ in enumerate(s):
            occurences[s_] += 1
            while (j-i+1) - max(occurences.values()) > k:
                occurences[s[i]] -= 1
                i += 1
            max_len = max(max_len,j-i+1)
        return max_len