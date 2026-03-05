# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = curr_streak = curr_num = 0
        ans = []
        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return
            
            dfs(node.left)

            num = node.val
            if curr_num == num:
                curr_streak += 1
            else:
                curr_num = num
                curr_streak = 1
            
            if curr_streak == max_streak:
                ans.append(num)
            elif curr_streak > max_streak:
                ans = [num]
                max_streak = curr_streak

            dfs(node.right)
        dfs(root)
        return ans