# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _,res = self.helper_(root)
        return res
    def helper_(self,root):
        if not root:
            return 0,True
        l_,res_l = self.helper_(root.left)
        r_,res_r = self.helper_(root.right)
        if not (res_l & res_r):
            return 0,False
        if abs(l_-r_) > 1:
            return 0,False
        return max(l_,r_)+1,True
        