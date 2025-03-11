"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dit = {}
        def dfs(node):
            if node is None:
                return None
            
            if node.val in dit:
                return dit[node.val]
            
            newNode = Node(node.val)

            dit[node.val] = newNode

            for subNode in node.neighbors:
                newNode.neighbors.append(dfs(subNode))
            
            return newNode
        
        return dfs(node)