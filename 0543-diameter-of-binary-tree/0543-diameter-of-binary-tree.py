# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _,total_len = self.helper_(root)
        return total_len
    
    def helper_(self,root):
        if root:
            if not root.left:
                l_, l_total = 0,0
            else:
                l_,l_total = self.helper_(root.left)
            if not root.right:
                r_, r_total = 0,0
            else:
                r_,r_total = self.helper_(root.right)
            new_ = max(l_ + (0 if root.left is None else 1),r_ +(0 if root.right is None else 1))
            new_total = max(r_total,l_total,l_ + r_ + (0 if (root.left is None) else 1) + (0 if (root.right is None) else 1))
            return new_,new_total
        else:
            return 0,0