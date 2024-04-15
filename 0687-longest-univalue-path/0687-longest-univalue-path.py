# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def dfs(self, root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if root.left != None and root.right != None and root.val == root.left.val and root.val == root.right.val:
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        elif root.left != None and root.left.val == root.val:
            self.ans = max(self.ans, left)
            return left + 1
        elif root.right != None and root.right.val == root.val:
            self.ans = max(self.ans, right)
            return right + 1
        else:
            return 1
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans