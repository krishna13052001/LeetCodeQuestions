# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)
        if root.val == 2:
            return right_result or left_result
        elif root.val == 3:
            return left_result and right_result
        if root.val == 0:
            return False
        return True