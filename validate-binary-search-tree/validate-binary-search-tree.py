import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root,min_value,max_value):
        if not root:
            return True
        # print(root)
        if(min_value< root.val and max_value>root.val):
            if (self.find(root.left,min_value,root.val) and self.find(root.right,root.val,max_value)):
                return True
            else:
                return False
        else:
            return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.find(root,-1*sys.maxsize, sys.maxsize)