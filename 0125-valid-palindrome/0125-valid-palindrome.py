class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        letters = set(range(ord('a'),ord('z')+1)).union(set(range(ord('0'),ord('9')+1)))
        while(i<j):
            temp_i = s[i]
            temp_j = s[j]
            if not ord(temp_i.lower()) in letters:
                i += 1
                continue
            if not ord(temp_j.lower()) in letters:
                j -= 1
                continue
            if temp_i.lower() != temp_j.lower():
                return False
            i += 1
            j -= 1
        return True