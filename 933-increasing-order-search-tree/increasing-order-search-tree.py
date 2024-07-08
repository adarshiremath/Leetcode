# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        visited = []
        def dfs(root):
            if root:
                dfs(root.left)
                visited.append(root.val)
                dfs(root.right)
        dfs(root)
        head = TreeNode(visited[0])
        dummy = head
        for i in visited[1:]:
            new1 = TreeNode(i)
            dummy.right = new1
            dummy = dummy.right
        return head
            