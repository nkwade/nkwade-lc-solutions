# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True #assume the tree is balanced
        
        def depth(node):
            if not node:#if the node is null then do not add it to the depth
                return 0
            l_depth = depth(node.left) #find the left depth
            r_depth = depth(node.right)#right the right depth
            
            if abs(l_depth - r_depth) > 1:#if the difference in depths is greater than 1 then it is not balanced
                self.res = False #tree is not balanced
            
            return 1 + max(l_depth, r_depth) #add the current node plus the max of the left and right depths
        depth(root)#call function
        return self.res#return if the tree is balanced