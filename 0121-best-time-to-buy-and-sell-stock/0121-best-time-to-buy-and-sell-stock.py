class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        curr_max = 0
        for idx in range(1,len(prices)):
            price = prices[idx]
            minimum = min(minimum,price)
            curr_max = max(curr_max,price-minimum)
        return curr_max
        