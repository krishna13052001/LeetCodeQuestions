# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root

    def next(self) -> int:
        curr = self.curr
        while curr:
            if not curr.left:
                self.curr = curr.right
                return curr.val
            else:
                successor = curr.left
                while successor.right and successor.right != curr:
                    successor = successor.right
                
                if not successor.right:
                    successor.right = curr
                    curr = curr.left
                else:
                    successor.right = None
                    self.curr = curr.right
                    return curr.val


    def hasNext(self) -> bool:
        if not self.curr:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()