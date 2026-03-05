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
        curr = root
        while curr:
            if curr.left == None:
                print(curr.val)
                if curr.val == curr_num:
                    curr_streak += 1
                else:
                    curr_num = curr.val
                    curr_streak = 1
                if curr_streak == max_streak:
                    ans.append(curr.val)
                elif curr_streak > max_streak:
                    ans = [curr.val]
                    max_streak = curr_streak
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    if curr.val == curr_num:
                        curr_streak += 1
                    else:
                        curr_num = curr.val
                        curr_streak = 1
                    if curr_streak == max_streak:
                        ans.append(curr.val)
                    elif curr_streak > max_streak:
                        ans = [curr.val]
                        max_streak = curr_streak
                    curr = curr.right
        return ans