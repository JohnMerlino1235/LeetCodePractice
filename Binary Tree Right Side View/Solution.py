# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = {}

        def dfs(root, level):
            if root:
                if level not in vals:
                    vals[level] = root.val
                dfs(root.right, level + 1)
                dfs(root.left, level + 1)

            return vals

        vals = dfs(root, 0)
        return vals.values()