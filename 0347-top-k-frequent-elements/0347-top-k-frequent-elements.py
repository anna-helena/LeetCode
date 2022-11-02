from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        H = [(-1*frequ,num) for num,frequ in seen.items()]
        heapq.heapify(H)
        sol = []
        for i in range(k):
            temp = heapq.heappop(H)
            sol.append(temp[1])
        return sol