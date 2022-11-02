from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for s_ in s:
            seen[s_] += 1
        for t_ in t:
            seen[t_] -= 1
            if seen[t_] == -1:
                return False
            if seen[t_] == 0:
                del seen[t_]
        return len(seen) == 0
        