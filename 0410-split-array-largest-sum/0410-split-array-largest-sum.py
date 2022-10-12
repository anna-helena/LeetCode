class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #split at idx
        #dp: dp(arr,k) = max(dp(arr[:idx],k-1),sum(arr[idx:]))
        #do it for idx = len(arr)-1 to ....k-1 or until sum is bigger than the other dp
        #maybe start with idx at fraction of sum just under it
        seen = {}
        def dp_sol(nums,k,seen):
            if k == 1:
                return sum(nums)
            idx_start = len(nums)-1
            fraction = sum(nums)//k
            while (sum(nums[idx_start:])<=fraction) & (idx_start>=k):
                  idx_start -= 1
            idx_start = min(len(nums)-1,idx_start+1)
            max_total = float('inf')
            while(idx_start >= k-1):
                max_rechts = sum(nums[idx_start:])
                if (idx_start,k) in seen:
                    max_links = seen[(idx_start,k)]
                else:
                    max_links = dp_sol(nums[:idx_start],k-1,seen)
                    seen[(idx_start,k)] = max_links
                new_max = max(max_links,max_rechts)
                max_total = min(new_max,max_total)
                if max_total == fraction:
                    return fraction
                if(max_links < max_rechts):
                    break
                idx_start -= 1
            return max_total
        return dp_sol(nums,k,seen)
    
                  