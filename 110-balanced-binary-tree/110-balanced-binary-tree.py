# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        
        def depth(node):
            if not node:
                return 0
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            
            if abs(l_depth - r_depth) > 1:
                self.res = False
            
            return 1 + max(l_depth, r_depth)
        depth(root)
        return self.res