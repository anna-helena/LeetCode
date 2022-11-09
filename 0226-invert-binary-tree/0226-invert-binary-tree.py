# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper_(root)
    def helper_(self,root):
        if root:
            root.left, root.right = self.helper_(root.right), self.helper_(root.left)
        return root
        