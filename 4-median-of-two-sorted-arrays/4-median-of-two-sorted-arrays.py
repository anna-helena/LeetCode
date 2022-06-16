from bisect import bisect_right

class Solution:
    #find two values (that fulfill >= idx) for generalized median search 
    #binary search the value, use bisect to know "where" we are at
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        mn = min(nums1[0] if nums1 else float('inf'), nums2[0] if nums2 else float('inf'))
        mx = max(nums1[-1] if nums1 else float('-inf'), nums2[-1] if nums2 else float('-inf'))
        print(mn,mx)
        def findNthElement(N):
            print('in fct')
            lo,hi = mn,mx
            el = lo
            while(lo <= hi):
                mid = (lo+hi)//2
                print(mid)
                res = bisect_right(nums1,mid) + bisect_right(nums2,mid)
                print(('res',res))
                if res >= N:
                    el = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return el
        
        first_el = findNthElement(N//2+1)
        second_el = findNthElement((N-1)//2+1)
        print(N//2+1,(N-1)//2+1)
        print(first_el,second_el)
        return(0.5*(first_el+second_el))
    