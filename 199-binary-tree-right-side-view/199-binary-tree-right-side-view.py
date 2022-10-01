# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        out = []
        
        queue = collections.deque([root])
        
        while queue:
            right = None
            len_q = len(queue)
            
            for i in range(len_q):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right:
                out.append(right.val)
        return out
            
            
        
        