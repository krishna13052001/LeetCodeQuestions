# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, Dict
class Solution:
    def markParentsAndGetStartNode(self, root: Optional[TreeNode], start: int) -> tuple[Dict, TreeNode]:
        parents = {}
        if not root:
            return parents, None
        
        q = deque([root])
        start_node = None
        while q:
            node = q.popleft()
            if node.val == start:
                start_node = node
            if node.left:
                parents[node.left] = node
                q.append(node.left)
            if node.right:
                parents[node.right] = node
                q.append(node.right)
        return parents, start_node
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents, startNode = self.markParentsAndGetStartNode(root, start)
        visited = set([startNode])
        q = deque([(startNode, 0)])
        result = -1
        while q:
            node, dist = q.popleft()
            result = max(result, dist)
            p = parents.get(node, None)
            if p and p not in visited:
                q.append((p, dist + 1))
                visited.add(p)
            if node.left and node.left not in visited:
                q.append((node.left, dist + 1))
                visited.add(node.left)
            if node.right and node.right not in visited:
                q.append((node.right, dist + 1))
                visited.add(node.right)
        return result
            