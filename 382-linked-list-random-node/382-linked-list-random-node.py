# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
    length = 0
    head = None
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        temp = head
        while(temp):
            self.length += 1
            temp = temp.next

    def getRandom(self) -> int:
        idx = random.randint(0,self.length-1)
        temp = self.head
        i = 0
        while(i<idx):
            i += 1
            temp = temp.next
        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()