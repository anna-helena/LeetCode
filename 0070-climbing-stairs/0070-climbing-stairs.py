class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = self.climbStairs_helper(n)
        return i + j
    
    #counts distinct ways of climbing stairs for starting by one and starting by two
    def climbStairs_helper(self, n):
        if n == 0:
            return 0, 0
        if n == 1:
            return 1, 0
        prev_i, prev_j = self.climbStairs_helper(n-1)
        return prev_i + prev_j, prev_i
        
        