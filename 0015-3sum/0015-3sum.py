class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        seen = set()
        for idx,num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            two = self.gettwosum(nums[idx+1:],-1*num)
            if len(two) > 0:
                for t in two:
                    sol.add(tuple(sorted(t + [num])))
        return sol
    
    def gettwosum(self,nums,target):
        sol = []
        prev = set()
        for num in nums:
            if (target-num) in prev:
                sol.append([target-num,num])
            prev.add(num)
        return sol
    