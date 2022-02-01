# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def findAns(self,root):
        if(root == None):
            return 0
        left_side = self.findAns(root.left)
        right_side = self.findAns(root.right)
        self.res = max(self.res,left_side+right_side)
        print(self.res)
        return max(left_side,right_side)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findAns(root)
        return self.res
        