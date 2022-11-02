class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_left = [1] * (len(nums)+1)
        prod_right = [1] * (len(nums)+1)
        temp = 1
        for idx in range(len(nums)):
            temp *= nums[idx]
            prod_left[idx+1] = temp
         
        temp = 1
        for idx in range(len(nums)-1,-1,-1):
            temp *= nums[idx]
            prod_right[idx] = temp
        sol = []
        for idx in range(len(nums)):
            sol.append(prod_left[idx]*prod_right[idx+1])
        return sol
        