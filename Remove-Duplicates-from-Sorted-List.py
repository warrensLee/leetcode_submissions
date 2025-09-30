# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head                                  #keep track of where we are
        while current and current.next:                 #while current and next are not null
            if current.val == current.next.val:         # if value of current and next are equal
                current.next = current.next.next        # set next to the one after next
            else:
                current = current.next                  # otherwise set current to next and continue
        return head
