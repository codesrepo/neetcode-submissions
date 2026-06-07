# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        if prev.next:
            current = prev.next
            prev.next = None
            if not current.next:
                current.next = prev
                current.next.next = None
                head = current
                return head
        else:
            return head
        while current.next:
            temp = current.next
            current.next = prev
            prev=current
            current = temp
        current.next = prev
        return current


        