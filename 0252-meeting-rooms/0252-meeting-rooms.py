from sortedcontainers import SortedList
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = SortedList()
        prev2 = {}
        for interval in intervals:
            x,y = interval
            temp = prev.bisect_right(x)
            if temp != prev.bisect_left(y):
                return False
            if temp > 0:
                if prev[temp-1] in prev2:
                    return False
            prev.add(x)
            prev2[x] = 0
            prev.add(y)
        return True