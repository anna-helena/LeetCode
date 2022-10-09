from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #sort list and keep info of original idx
        #go from smallest to largest check how many bigger indices have already been seen
        #as you go you create a list of seen indices, with binary search add new index which tells 
        #you how many have been already seen to the right
        #nlogn
        
        sorted_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        nums = sorted(nums)
        seen = SortedList()
        result = [0]*len(nums)
        for i,val in enumerate(nums):
            idx = sorted_indices[i]
            #add to seen
            new_idx = seen.bisect_right(idx)
            result[idx] = len(seen) - new_idx
            seen.add(idx)
        return result