# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        visited = []
        
        def dfs(root):
            if root:
                if root.val >= low and root.val <= high:
                    visited.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        
        return sum(visited)