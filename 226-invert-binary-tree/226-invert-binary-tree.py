# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #return self.iterative(root)
        return self.recursive(root)
    
    def iterative(self, root):
        return Non
    def recursive(self, root): 
        if not root:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.recursive(root.left)
        self.recursive(root.right)
        return root