# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_of_nodes(self,root, currentSum):
        if root == None:
            return 0
        currentSum = currentSum * 10 + root.val
        if root.left == None and root.right == None:
            return currentSum
        leftSum = self.sum_of_nodes(root.left,currentSum)
        rightSum = self.sum_of_nodes(root.right, currentSum)
        return leftSum + rightSum
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum_of_nodes(root, 0)