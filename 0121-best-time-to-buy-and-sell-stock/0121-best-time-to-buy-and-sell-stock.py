class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        curr_max = 0
        for idx in range(1,len(prices)):
            minimum = min(minimum,prices[idx])
            curr_max = max(curr_max,prices[idx]-minimum)
        return curr_max
        