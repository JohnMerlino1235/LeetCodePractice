# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_lca(root, v1, v2):
            if root == None:
                return None

            if v1 < root.val and v2 < root.val:
                return get_lca(root.left, v1, v2)
            elif v1 > root.val and v2 > root.val:
                return get_lca(root.right, v1, v2)
            else:
                return root

        return get_lca(root, p.val, q.val)