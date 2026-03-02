# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(head: Optional[TreeNode]) -> int:
            if head == None:
                return 0
            left = find_height(head.left)
            right = find_height(head.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) >= 2:
                return -1
            return max(left, right) + 1
        return find_height(root) != -1
