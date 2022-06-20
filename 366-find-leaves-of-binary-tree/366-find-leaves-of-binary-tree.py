# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        depths = {}
        max_val = self.helper_fct(root,depths)
        for val in range(0,max_val):
            result.append(depths[val])
        return result
    
    def helper_fct(self, root,depths):
        if not root:
            return 0
        d_l = self.helper_fct(root.left,depths)
        d_r = self.helper_fct(root.right,depths)
        d_max = max(d_l,d_r)
        if d_max in depths:
            temp = depths[d_max]
            temp.append(root.val)
            depths[d_max] = temp
        else:
            depths[d_max] = [root.val]
        return d_max + 1
        
        
        
        