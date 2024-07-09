# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        lis = []
        holder = []
        def dfs(root):
            if root:
                holder.append(str(root.val))
                if not root.left and not root.right:
                    lis.append(int("".join(holder), 2))
                dfs(root.left)
                dfs(root.right)
                holder.pop()
        dfs(root)
        return sum(lis)
                                    