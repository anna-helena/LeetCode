class Solution:
    def __init__(self):
        self.seen = {}
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        if n in self.seen:
            return self.seen[n]
        one_ = self.climbStairs(n-1) 
        two_ = self.climbStairs(n-2)
        self.seen[n] = max(one_,1) + max(two_,1)
        return max(one_,1) + max(two_,1)
        