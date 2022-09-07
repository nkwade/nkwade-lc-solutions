# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        
        def depthSearch(node):
            if not node:
                return 0
            l_depth = depthSearch(node.left)
            r_depth = depthSearch(node.right)
            self.max_d = max(self.max_d, l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        
        depthSearch(root)
        return self.max_d