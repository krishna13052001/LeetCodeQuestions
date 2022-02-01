# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float("-inf")
    def findAns(self,root):
        if not root:
            return 0
        left_side = max(0,self.findAns(root.left))
        right_side = max(0,self.findAns(root.right))
        self.res = max(self.res,left_side+right_side+root.val)
        return max(left_side+root.val,right_side+root.val)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findAns(root)
        return self.res