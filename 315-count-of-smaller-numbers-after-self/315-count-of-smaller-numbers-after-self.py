from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #sort list and keep info of original idx
        #go from smallest to largest check how many bigger indices have already been seen
        #as you go you create a list of seen indices, with binary search add new index which tells 
        #you how many have been already seen to the right
        #nlogn
        
        #sorted_dict = {nums[idx]: idx for idx in sorted(range(len(nums)), key=lambda k: nums[k])}
        sorted_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        nums = sorted(nums)
        print(sorted_indices)
        seen = SortedList()
        result = [0]*len(nums)
        for i,val in enumerate(nums):
            idx = sorted_indices[i]
            #add to seen
            new_idx = seen.bisect_right(idx)
            if((len(seen) - new_idx)==9):
                print(seen,new_idx,idx,val)
            result[idx] = len(seen) - new_idx
            seen.add(idx)
            if((len(seen) - new_idx)==10):
                print(result)
        return result