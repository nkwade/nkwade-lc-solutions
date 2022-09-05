"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(level)
        return res