class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #adapted binary search
        lo = 1
        hi = len(arr) - 2
        if hi == 1:
            return 1
        while(lo <= hi):
            mid = (lo + hi)//2
            #if mid < mountain
            if arr[mid+1]>arr[mid]:
                lo = mid + 1
            #if mid > mountain
            elif arr[mid-1]>arr[mid]:
                hi = mid - 1
            #if mid == mountain -> return mid
            else:
                return mid
        return lo