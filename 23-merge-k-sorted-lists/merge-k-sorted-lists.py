# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sortedcontainers import SortedList
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = SortedList()
        for i in lists:
            while i:
                l.add(i.val)
                i = i.next
        if len(l) == 0:
            return 
        head = ListNode()
        dummy = head
        for i in l[:-1]:
            dummy.val = i
            dummy.next = ListNode()
            dummy = dummy.next
        dummy.val = l[-1]
        return head
