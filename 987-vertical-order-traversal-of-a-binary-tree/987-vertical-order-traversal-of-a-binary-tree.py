# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list) #creates a hashmap for the the columns of values
        
        queue = [ (root, 0, 0) ] #initializes a queue with the root position and depth, this is how to start bfs
        
        while queue: #while we have not traversed the entire tree
            node, pos, depth = queue.pop(0) #gets the node its pos and depth
            if not node: continue #if it was null then just go to the next iteration of the loop
            results[(pos,depth)].append(node.val) #append the node to the hashmap where its x and y in the grid is its key
            results[(pos,depth)].sort() #i dont understand why it has to be sorted there will only be 1 value in each key
            queue.extend( [ (node.left, pos-1, depth+1), (node.right, pos+1, depth+1) ] )
            
            
        res = defaultdict(list)
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))
        
        
        for k in keys:
            pos, depth = k
            res[pos].extend(results[k])

        return res.values()