class Solution:
    def findKthNode(self, node, k):
        k -= 1
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        prevGroupTail = dummy
        temp = head

        while temp:
            kth = self.findKthNode(temp, k)
            if not kth:
                prevGroupTail.next = temp
                break

            nextGroupHead = kth.next
            kth.next = None
            prev, curr = None, temp
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            prevGroupTail.next = prev
            prevGroupTail = temp
            temp = nextGroupHead

        return dummy.next
