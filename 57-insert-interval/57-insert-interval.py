class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a,b = newInterval
        #find binary sect a
        #find binary sect b
        #combine where needed
        
        #biect_left
        def find_index_higher_equal(val,left=True):
            if left:
                i = 0
            else:
                i = 1
            lo = 0
            hi = len(intervals)
            while(lo < hi):
                mid = (lo + hi)//2
                temp = intervals[mid][i]
                if val > temp:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        i_a = find_index_higher_equal(a,False)
        i_b = find_index_higher_equal(b,True)
        #define new interval and add
        if intervals:
            if(i_a<len(intervals)):
                newInterval[0] = min(a,intervals[i_a][0])
            else:
                newInterval[0] = a
            if (i_b < len(intervals)):
                if (intervals[i_b][0] == b):
                    temp_i_b = i_b
                else:
                    temp_i_b = i_b-1
            else:
                temp_i_b = i_b-1
            if(temp_i_b>=0):
                newInterval[1] = max(b,intervals[temp_i_b][1])
            else:
                newInterval[1] = b
        else:
            temp_i_b = 0
            #delete not needed intervals
            #del intervals[(i_a):(temp_i_b+1)]
        #intervals.insert(i_a,newInterval)
        
        return intervals[:i_a] + [newInterval] + intervals[(temp_i_b+1):]