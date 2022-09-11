"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}#map the old nodes to their newly created copies
        
        def create(node): #creates a node
            if node in oldToNew: #if the node has already been copied
                return oldToNew[node] #return that copied node
            copy = Node(node.val) #create a new node
            oldToNew[node] = copy #map the old node to the copied node
            for neighbor in node.neighbors: #copy all the neighbors
                copy.neighbors.append(create(neighbor)) #recursive create the neighbor node
            
            return copy#return the newly created node
        
        return create(node) if node else None #return the head node 