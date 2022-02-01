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
        # print("Values",left_side,right_side)
        if(left_side == -1 or right_side == -1):
            return -1
        if(abs(left_side-right_side)>1):
            return -1
        # print(max(left_side,right_side)+1)
        return max(left_side,right_side)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.findAns(root)
        if(res == -1):
            return False
        return True