from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        H = []
        for s_ in seen:
            H.append((-1*seen[s_],s_))
        heapq.heapify(H)
        sol = []
        print(H)
        for i in range(k):
            temp = heapq.heappop(H)
            sol.append(temp[1])
        return sol