# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []

        def bfs(root):
            q = deque()
            q.append(root)

            while q:
                ans = []
                for _ in range(len(q)):
                    node = q.popleft()
                    ans.append(node.val)
                    if node.left != None:
                        q.append(node.left)
                    if node.right != None:
                        q.append(node.right)
                res.append(ans)
        
        bfs(root)
        return res
