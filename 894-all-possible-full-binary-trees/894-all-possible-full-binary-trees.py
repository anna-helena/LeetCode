# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        
        all_trees = [[]]*(n+1)
        def get_all_trees(n):
            new_tree_list = []
            if len(all_trees[n]) != 0:
                return all_trees[n]
            if n == 1:
                tree = TreeNode()
                new_tree_list.append(tree)
            else:
                for l in range(1,n-1,2):
                    l_list = get_all_trees(l)
                    r_list = get_all_trees((n-1)-l)
                    for l_ in l_list:
                        for r_ in r_list:
                            tree = TreeNode()
                            tree.left = l_
                            tree.right = r_
                            new_tree_list.append(tree)
            all_trees[n] = new_tree_list
            return new_tree_list
        
        return get_all_trees(n)