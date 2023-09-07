# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head
        ll = []

        while dummy:
            ll.append(dummy.val)
            dummy = dummy.next
        l = ll[:left-1]
        c = ll[left-1:right][::-1]
        r = ll[right:]
        c.extend(r)
        l.extend(c)
        ll = l
        dummy = head
        i = 0
        while dummy:
            dummy.val = ll[i]
            i += 1
            dummy = dummy.next
        return head