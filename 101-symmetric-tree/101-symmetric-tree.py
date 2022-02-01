# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.findAns(root.left,root.right)
    
    def findAns(self,l,r):
        if not l and not r:
            return True
        try:
            if(l and r and l.val ==r.val and self.findAns(l.left,r.right) and self.findAns(l.right,r.left)):
                return True
        except:
            return False
        return False