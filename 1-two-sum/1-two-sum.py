class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop through array, build a hash of what needed as key amd value indes
        #check if what is needed is at current index
        
        needed = {}
        for idx, val  in enumerate(nums):
            if val in needed:
                return [needed[val], idx]
            else:
                needed[target - val] = idx
                
        