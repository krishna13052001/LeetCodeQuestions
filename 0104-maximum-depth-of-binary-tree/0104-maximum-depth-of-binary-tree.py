# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_height(head: Optional[TreeNode]) -> int:
            if head == None:
                return 0
            left = find_height(head.left)
            right = find_height(head.right)
            return 1 + max(left, right)
        return find_height(root)