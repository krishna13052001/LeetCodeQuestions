# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        prev = None
        def find_ans(node):
            if not node:
                return 
            nonlocal prev
            find_ans(node.right)
            find_ans(node.left)
            node.right = prev
            node.left = None
            prev = node
        find_ans(root)
        