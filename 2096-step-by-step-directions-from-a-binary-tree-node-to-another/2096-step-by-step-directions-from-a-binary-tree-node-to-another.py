# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        #find path to s, find path to t
        #remove equal path until node P
        #go from s up to P and then to t down
        
        path = {}
        stack = []
        stack.append(root)
        path[root.val] = (None,None,False)
        number_seen = 0
        while stack:
            curr = stack.pop()
            val = curr.val
            (prev,where,seen) = path[val]
            if seen == True:
                continue
            if((val == startValue) | (val == destValue)):
                number_seen += 1
                if number_seen == 2:
                    break
            seen = True
            path[val] = (prev,where,seen)
            if(curr.left):
                l_ = curr.left
                stack.append(l_)
                path[l_.val] = (val,'L',False)
            if(curr.right):
                r_ = curr.right
                stack.append(r_)
                path[r_.val] = (val,'R',False)
        path_s = []
        path_t = []
        val = startValue
        while val:
            (next_val,where,_) = path[val]
            path_s.append(where)
            val = next_val
        val = destValue
        while val:
            (next_val,where,_) = path[val]
            path_t.append(where)
            val = next_val   
        #eliminate start
        if((len(path_s)>0) & (len(path_t)>0)):
            last_s = path_s[-1]
            last_t = path_t[-1]
            while(last_s == last_t):
                path_s.pop()
                path_t.pop()
                if((len(path_s)==0) | (len(path_t)==0)):
                    break
                last_s = path_s[-1]
                last_t = path_t[-1]
        result = "U"*len(path_s)
        for i in range(len(path_t)-1,-1,-1):
            result += path_t[i]
        return result
        
        