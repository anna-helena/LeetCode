class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {'(':')','[':']','{':'}'}
        stack = []
        for s_ in s:
            if s_ in open_close:
                stack.append(s_)
            elif stack:
                if s_ != open_close[stack.pop()]:
                    return False
            else:
                return False
        if stack:
            return False
        return True