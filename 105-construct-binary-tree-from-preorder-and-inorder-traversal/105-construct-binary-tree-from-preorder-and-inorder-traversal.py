# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    root = preorder[0]
    
    def array_to_tree(left, right):
      nonlocal preorder_index
      if left > right: return None
      
      root = TreeNode(preorder[preorder_index])
      
      preorder_index += 1
      
      root.left = array_to_tree(left, inorder_index_map[root.val] - 1)
      root.right = array_to_tree(inorder_index_map[root.val] + 1, right)
      
      return root
    
    preorder_index = 0
    
    inorder_index_map = {}
    for index, value in enumerate(inorder):
      inorder_index_map[value] = index
      
    return array_to_tree(0, len(preorder) - 1)