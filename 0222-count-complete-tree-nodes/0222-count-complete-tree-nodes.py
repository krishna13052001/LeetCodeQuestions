# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeightLeft(self,root) -> int:
        height = 0
        while root:
            height += 1
            root = root.left
        return height
    def findHeightRight(self,root) -> int:
        height = 0
        while root:
            height += 1
            root = root.right
        return height
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.findHeightLeft(root)
        right = self.findHeightRight(root)
        if left == right:
            return (1 << left) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)