from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            
            queue.append(left.left if left else None)
            queue.append(right.right if right else None)
            queue.append(left.right if left else None)
            queue.append(right.left if right else None)
        return True