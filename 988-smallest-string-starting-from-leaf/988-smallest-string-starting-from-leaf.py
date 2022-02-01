from typing import Tuple
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mn: Tuple[int] = None
        print(self.mn)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root, deque())
        if not self.mn:
            return ""
        return "".join(chr(e + ord("a")) for e in self.mn)
    def dfs(self,node,cur_deque):
        if not node:
            return
        cur_deque.appendleft(node.val)
        if not node.left and not node.right:
            t = tuple(cur_deque)
            print(cur_deque,t)
            if not self.mn or t<self.mn:
                self.mn=t
        else:
            self.dfs(node.left,cur_deque)
            self.dfs(node.right,cur_deque)
        cur_deque.popleft()