import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        max_heap = [-1*x for x in nums]
        heapq.heapify(max_heap)
        self.k_largest = []
        for i in range(k):
            if max_heap:
                heapq.heappush(self.k_largest,heapq.heappop(max_heap)*-1)
        self.k = k

    def add(self, val: int) -> int:
        if (len(self.k_largest) < self.k):
            heapq.heappush(self.k_largest,val)
        elif (val > self.k_largest[0]):
            heapq.heappop(self.k_largest)
            heapq.heappush(self.k_largest,val)
        return self.k_largest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)