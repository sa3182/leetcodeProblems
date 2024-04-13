class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        before_head = merge = ListNode()

        while(list1 and list2):
            if list1.val < list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                 merge.next = list2
                 list2 = list2.next
            merge = merge.next
        merge.next = list1 or list2

        return before_head.next
