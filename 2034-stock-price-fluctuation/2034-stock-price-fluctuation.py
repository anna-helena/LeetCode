import heapq

class StockPrice:

    def __init__(self):
        self.prices = {}
        self.nr_prices = {}
        self.latest = float('-inf')
        self.max_val = []
        self.min_val= []
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.prices:
            self.latest = max(self.latest, timestamp)
        else:
            prev = self.prices[timestamp]
            temp = self.nr_prices[prev]
            if temp == 1:
                del self.nr_prices[prev]
            else:
                self.nr_prices[prev] = temp - 1
        heapq.heappush(self.min_val,price)
        heapq.heappush(self.max_val,-1*price)
        self.prices[timestamp] = price
        if price in self.nr_prices:
            temp = self.nr_prices[price] 
            self.nr_prices[price] = temp + 1
        else:
            self.nr_prices[price] = 1
            
            

    def current(self) -> int:
        if self.latest > 0:
            return self.prices[self.latest]
        return 0

    def maximum(self) -> int:
        while self.max_val:
            temp = -1*self.max_val[0]
            if (temp in self.nr_prices):
                return temp
            else:
                heapq.heappop(self.max_val)
        return

    def minimum(self) -> int:
        while self.min_val:
            temp = self.min_val[0]
            if temp in self.nr_prices:
                return self.min_val[0]
            else:
                heapq.heappop(self.min_val)
        return


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()