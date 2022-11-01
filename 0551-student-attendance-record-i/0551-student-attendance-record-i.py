class Solution:
    def checkRecord(self, s: str) -> bool:
        L = 0
        A = False
        for s_ in s:
            if s_ == 'L':
                L += 1
                if L == 3:
                    return False
            else:
                L = 0
                if s_ == 'A':
                    if A:
                        return False
                    A = True
        return True
        