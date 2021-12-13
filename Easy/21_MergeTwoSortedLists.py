# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        curr = output
        curr1 = list1
        curr2 = list2
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                new_next = curr1.next
                curr.next = curr1
                curr1 = new_next
            else:
                new_next = curr2.next
                curr.next = curr2
                curr2 = new_next
            curr = curr.next
        if curr1 is not None:
            curr.next = curr1
        else:
            curr.next = curr2
        return output.next
            
