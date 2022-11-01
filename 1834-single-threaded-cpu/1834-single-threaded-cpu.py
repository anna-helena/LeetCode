import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []
        for idx,task in enumerate(tasks):
            enqueue.append((task[0],idx))
        heapq.heapify(enqueue)
        time = enqueue[0][0]
        consider = []
        sol = []
        while enqueue:
            while enqueue[0][0] <= time:
                temp = heapq.heappop(enqueue)
                new_consider = (tasks[temp[1]][1],temp[1])
                heapq.heappush(consider,new_consider)
                if len(enqueue) == 0:
                    break
            if len(consider) > 0:
                next_consider = heapq.heappop(consider)
                sol.append(next_consider[1])
                time += next_consider[0]
            else:
                time = enqueue[0][0]
        while consider:
            next_consider = heapq.heappop(consider)
            sol.append(next_consider[1])
        return sol
        