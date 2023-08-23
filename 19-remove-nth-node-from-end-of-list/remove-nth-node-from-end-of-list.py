# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= head
        count = 0
        while dummy:
            count += 1
            dummy = dummy.next
        if n == count:
            return head.next
        nth = count - n
        print(nth)
        dummy = head
        count = 0
        while dummy:
            if count == nth-1:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
            count += 1
        return head