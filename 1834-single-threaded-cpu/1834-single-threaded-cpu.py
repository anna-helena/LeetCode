import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []
        for idx,task in enumerate(tasks):
            enqueue.append((task[0],idx))
        heapq.heapify(enqueue)
        enqueue = [(enq,process,idx) for idx, (enq,process) in enumerate(tasks)]
        enqueue.sort()
        time = enqueue[0][0]
        consider = []
        sol = []
        idx_start = 0
        while idx_start < len(enqueue):
            while enqueue[idx_start][0] <= time:
                new_consider = (enqueue[idx_start][1],enqueue[idx_start][2])
                heapq.heappush(consider,new_consider)
                idx_start += 1
                if idx_start == len(enqueue):
                    break
            if len(consider) > 0:
                next_consider = heapq.heappop(consider)
                sol.append(next_consider[1])
                time += next_consider[0]
            else:
                time = enqueue[idx_start][0]
        while consider:
            next_consider = heapq.heappop(consider)
            sol.append(next_consider[1])
        return sol
        