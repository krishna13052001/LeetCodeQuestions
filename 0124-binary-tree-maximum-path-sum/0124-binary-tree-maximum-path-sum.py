# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def find_ans(head) -> int:
            if head == None:
                return 0
            left = find_ans(head.left)
            if left < 0:
                left = 0
            right = find_ans(head.right)
            if right < 0:
                right = 0
            self.res = max(self.res, left + right + head.val)
            return max(left, right) + head.val
        find_ans(root)
        return self.res