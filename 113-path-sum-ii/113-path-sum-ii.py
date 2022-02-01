# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.accumulatePathSum(root, targetSum, [], result)
        return result
    def accumulatePathSum(self, root, sum, cur_path, result):
        if not root:
            return
        sum = sum - root.val
        cur_path.append(root.val)
        if sum==0 and root.left is None and root.right is None:
            result.append(list(cur_path))
            return

        if root.left: 
            self.accumulatePathSum(root.left, sum, list(cur_path), result)
        if root.right: 
            self.accumulatePathSum(root.right, sum, list(cur_path), result)