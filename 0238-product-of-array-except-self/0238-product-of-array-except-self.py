class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * (len(nums))
        temp = 1
        for idx in range(len(nums)):
            sol[idx] = temp
            temp *= nums[idx]
        temp = 1
        for idx in range(len(nums)-1,-1,-1):
            sol[idx] *= temp
            temp *= nums[idx]
        return sol
        