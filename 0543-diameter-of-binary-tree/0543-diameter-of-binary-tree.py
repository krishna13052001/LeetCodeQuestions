# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = -1
        def find_ans(head: Optional[TreeNode]) -> int:
            if head == None:
                return 0
            left = find_ans(head.left)
            right = find_ans(head.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        find_ans(root)
        return self.res