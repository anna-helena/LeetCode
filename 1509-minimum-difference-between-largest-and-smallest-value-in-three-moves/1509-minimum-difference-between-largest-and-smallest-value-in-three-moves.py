class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #[0,1,5,10,14]
        #sort the array
        #go with smalles, largest index, and count 3 "jumps" always biggest diff, then return max_diff
        #trivial when len <= 4
        if len(nums) <= 4:
	        return 0
        nums.sort()
        return min(nums[-4]-nums[0],nums[-3]-nums[1],nums[-2]-nums[2],nums[-1]-nums[3])