"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #build hash where key = id, val = idx
        #to bfs or dfs to get all
        id_hash = {}
        seen = set()
        for i,e in enumerate(employees):
            id_hash[e.id] = i
        total_imp = 0
        toSee = []
        toSee.append(id)
        while toSee:
            currId = toSee.pop()
            if currId in seen:
                continue
            else:
                seen.add(currId)
            currE = employees[id_hash[currId]]
            total_imp += currE.importance
            #add subord to tosee list
            for sub in currE.subordinates:
                toSee.append(sub)
        return total_imp
        