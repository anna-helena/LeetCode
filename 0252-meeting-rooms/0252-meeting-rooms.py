class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = set()
        for interval in intervals:
            start, finish = interval
            for i in range(start+1,finish):
                if i in prev:
                    return False
            else:
                for i in range(start,finish+1):
                    prev.add(i)
        return True