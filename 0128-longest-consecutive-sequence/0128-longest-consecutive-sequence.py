class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev = {}
        max_len = 1
        for num in nums:
            if num in prev:
                continue
            if ((num-1) in prev) & ((num+1) in prev):
                temp_len,temp_start,temp_end = prev[num-1]
                temp_len2,temp_start2,temp_end2 = prev[num+1]
                prev[num] = (temp_len+temp_len2+1,temp_start,temp_end2)
                prev[temp_start] = (temp_len+temp_len2+1,temp_start,temp_end2)
                prev[temp_end2] = (temp_len+temp_len2+1,temp_start,temp_end2)
                max_len = max(max_len,temp_len+temp_len2+1)
            elif (num-1) in prev:
                temp_len,temp_start,temp_end = prev[num-1]
                prev[num] = (temp_len+1,temp_start,num)
                prev[temp_start] = (temp_len+1,temp_start,num)
                max_len = max(max_len,temp_len+1)
            elif (num+1) in prev:
                temp_len,temp_start,temp_end = prev[num+1]
                prev[num] = (temp_len+1,num,temp_end)
                prev[temp_end] = (temp_len+1,num,temp_end)
                max_len = max(max_len,temp_len+1)
            else:
                prev[num] = (1,num,num)
        return max_len