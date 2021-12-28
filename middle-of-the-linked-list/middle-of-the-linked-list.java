/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = new ListNode();
        ListNode fast = new ListNode();
        slow = head;
        fast = head.next;
        while(fast != null && fast.next != null){
            slow = slow.next;
            // System.out.println(fast.next);
            fast = fast.next.next;
        }
        if(fast == null)
            return slow;
        else
            return slow.next;
    }
}