# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = SortedList()
        def inorder(root):
            if root:
                inorder(root.left)
                sorted_list.add(root.val)
                inorder(root.right)
        inorder(root)
        return sorted_list[k-1]