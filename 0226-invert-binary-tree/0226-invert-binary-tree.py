# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper_(root,'root')
    def helper_(self,root,where_from):
        if root:
            root.left, root.right = self.helper_(root.right,'right'), self.helper_(root.left,'left')
        return root
        