from sortedcontainers import SortedList
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = SortedList()
        prev2 = {}
        for interval in intervals:
            x,y = interval
            if prev.bisect_right(x) != prev.bisect_left(y):
                return False
            if prev.bisect_right(x) > 0:
                if prev[prev.bisect_right(x)-1] in prev2:
                    return False
            prev.add(x)
            prev2[x] = 0
            prev.add(y)
        return True