from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = defaultdict(int)
        for s1_ in s1:
            first[s1_] += 1
        i = 0
        while i < len(s2):
            if s2[i] not in first:
                i += 1
                continue
            temp = defaultdict(int)
            temp[s2[i]] += 1
            possible = True
            for j in range(1,len(s1)):
                if (i+j) < len(s2):
                    if s2[i+j] in first:
                        temp[s2[i+j]] += 1
                    else:
                        possible = False
                        i = i + j + 1
                        break
                else:
                    return False
            if possible:
                if temp == first:
                    return True
                i += 1
        return False
        