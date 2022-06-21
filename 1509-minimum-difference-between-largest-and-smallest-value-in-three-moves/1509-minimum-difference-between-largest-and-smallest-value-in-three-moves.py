class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #[0,1,5,10,14]
        #sort the array
        #go with smalles, largest index, and count 3 "jumps" always biggest diff, then return max_diff
        #trivial when len <= 4
        if(len(nums)<=4):
            return 0
        nums.sort()
        nr_consider = len(nums) - 3
        diff = nums[len(nums)-1] - nums[0]
        for i in range(0,len(nums)-nr_consider+1):
            diff_temp = nums[i+nr_consider-1] - nums[i]
            if diff_temp < diff:
                diff = diff_temp
        return diff
            
        