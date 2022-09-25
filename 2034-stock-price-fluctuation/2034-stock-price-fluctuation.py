import heapq

class StockPrice:

    def __init__(self):
        self.prices = {}
        self.latest = float('-inf')
        self.max_val = []
        self.min_val= []
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.prices:
            self.latest = max(self.latest, timestamp)
        heapq.heappush(self.min_val,(price,timestamp))
        heapq.heappush(self.max_val,(-1*price,timestamp))
        self.prices[timestamp] = price            

    def current(self) -> int:
        if self.latest > 0:
            return self.prices[self.latest]
        return 0

    def maximum(self) -> int:
        while self.max_val:
            (price_temp, time_temp) = self.max_val[0]
            if (self.prices[time_temp] == -1*price_temp):
                return -1*price_temp
            else:
                heapq.heappop(self.max_val)
        return

    def minimum(self) -> int:
        while self.min_val:
            (price_temp, time_temp) = self.min_val[0]
            if (self.prices[time_temp] == price_temp):
                return price_temp
            else:
                heapq.heappop(self.min_val)
        return


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()