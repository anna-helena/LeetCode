from collections import Counter

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            digits = Counter()
            while(n > 0):
                temp = n % 10
                digits[int(temp)] += 1
                n -= temp
                n /= 10
            temp_ = []
            for d in digits:
                temp_.append(str(d)+'_'+str(digits[d]))
            digits_ = frozenset(temp_)
            if digits_ in seen:
                return False
            seen.add(digits_)
            n = 0
            for d in digits:
                for i in range(1,digits[d]+1):
                    n += d*d
            if n == 1:
                return True
        