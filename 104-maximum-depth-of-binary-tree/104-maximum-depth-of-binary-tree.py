# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findAns(self,root):
        if not root:
            return 0
        left_side = self.findAns(root.left)
        right_side = self.findAns(root.right)
        return max(left_side,right_side)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findAns(root)