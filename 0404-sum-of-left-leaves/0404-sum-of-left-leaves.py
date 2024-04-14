# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(head,count):
            if head.left != None:
                if head.left.left == None and head.left.right == None:
                    count += head.left.val
                count = dfs(head.left,count)
            if head.right != None:
                count = dfs(head.right,count)
            return count
        return dfs(root,count)