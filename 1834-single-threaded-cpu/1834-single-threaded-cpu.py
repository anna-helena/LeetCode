import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enq,process,idx) for idx, (enq,process) in enumerate(tasks)]
        tasks.sort()
        time = tasks[0][0]
        consider = []
        sol = []
        idx_start = 0
        while idx_start < len(tasks):
            while tasks[idx_start][0] <= time:
                new_consider = (tasks[idx_start][1],tasks[idx_start][2])
                heapq.heappush(consider,new_consider)
                idx_start += 1
                if idx_start == len(tasks):
                    break
            if len(consider) > 0:
                next_consider = heapq.heappop(consider)
                sol.append(next_consider[1])
                time += next_consider[0]
            else:
                time = tasks[idx_start][0]
        while consider:
            next_consider = heapq.heappop(consider)
            sol.append(next_consider[1])
        return sol
        