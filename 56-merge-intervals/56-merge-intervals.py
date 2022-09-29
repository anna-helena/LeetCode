class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i,interval in enumerate(intervals):
            a,b = interval
            if (len(result) > 0):
                idx_a = self.bisect_l(a,result)
                idx_b = self.bisect_r(b,result)
                #check for merge left
                if((idx_a % 2) == 1):
                    interval[0] = result[idx_a//2][0]
                del_start = idx_a//2
                #check for merge right
                if((idx_b % 2) == 1):
                    interval[1] = result[idx_b//2][1]
                    del_end = idx_b//2
                else:
                    del_end = idx_b//2-1
                #delete all touched
                del result[(del_start):(del_end+1)]
                result.insert(idx_a//2, interval)
                
            else:
                result.append(interval)
        return result

    def bisect_l(self,x,a):
        lo = 0
        hi = len(a)*2
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid//2][mid%2] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def bisect_r(self,x,a):
        lo = 0
        hi = len(a)*2
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid//2][mid%2]:
                hi = mid
            else:
                lo = mid + 1
        return lo