class Solution:
    def numSplits(self, s: str) -> int:
        return self.helper_(s,set(),set())
    def helper_(self, rem, l, r):
        if len(rem) == 0:
            return 1
        if len(rem) == 1:
            count = 0
            if rem[0] in l:
                count += 1
            if rem[0] in r:
                count += 1
            return count
        l_i = 0
        r_i = len(rem)-1
        l.add(rem[l_i])
        r.add(rem[r_i])      
        while l_i < len(rem)-2:
            if rem[l_i+1] not in l:
                break
            l_i += 1
        r_i = len(rem)
        while r_i >= 2:
            if rem[r_i-1] not in r:
                break
            r_i -= 1
        if l_i >= r_i:
            return l_i-r_i+2 
        return self.helper_(rem[(l_i+1):r_i],l,r)
        
