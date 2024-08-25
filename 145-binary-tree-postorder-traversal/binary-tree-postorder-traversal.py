# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root, visited):
            if root:
                postorder(root.left, visited)
                postorder(root.right, visited)
                visited.append(root.val)
                return visited
        return postorder(root, [])
            