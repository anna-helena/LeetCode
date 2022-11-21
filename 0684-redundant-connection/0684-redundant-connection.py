class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        res = []
        for idx,[x,y] in enumerate(edges):
            if x not in parents:
                parents[x] = x
            if y not in parents:
                parents[y] = y
            temp = self.find_parent(x,parents)
            if temp == self.find_parent(y,parents):
                res = [x,y]
            else:
                parents[temp] = y
        return res
            
    
    def find_parent(self,node,parents):
        if parents[node] == node:
            return node
        return self.find_parent(parents[node],parents)
        
        