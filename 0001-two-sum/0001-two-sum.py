class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for idx,num in enumerate(nums):
            if num in prev:
                return [prev[num],idx]
            else:
                prev[target-num] = idx
        