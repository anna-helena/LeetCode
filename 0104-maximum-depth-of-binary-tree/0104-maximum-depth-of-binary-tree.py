# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)
        max_depth = max(depth_l,depth_r) + 1
        return max_depth