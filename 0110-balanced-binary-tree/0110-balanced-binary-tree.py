# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(head: Optional[TreeNode]) -> [bool, int]:
            if head == None:
                return True, 0
            is_balanced, left = find_height(head.left)
            if not is_balanced:
                return False, left
            is_balanced, right = find_height(head.right)
            if not is_balanced:
                return False, right
            if abs(left - right) >= 2:
                return False, 1 + max(left,right)
            else:
                return True, 1 + max(left, right)
        is_balanced, _ = find_height(root)
        return is_balanced
