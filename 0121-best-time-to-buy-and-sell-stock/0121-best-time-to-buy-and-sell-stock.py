class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        curr_max = 0
        for idx in range(1,len(prices)):
            price = prices[idx]
            if price < minimum:
                minimum = price
            else:
                curr_max = max(curr_max,price-minimum)
        return curr_max
        