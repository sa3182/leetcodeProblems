class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next== None:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        return head