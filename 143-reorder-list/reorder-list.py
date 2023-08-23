# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = head
        linked_list = []
        while dummy:
            linked_list.append(dummy.val)
            dummy = dummy.next
        length = len(linked_list)
        ll = []
        for i in range(len(linked_list)//2):
            ll.append(linked_list[i])
            ll.append(linked_list[length - i - 1])
        if length%2 != 0:
            ll.append(linked_list[length//2])
        count = 0
        dummy = head
        while dummy:
            dummy.val = ll[count]
            count += 1
            dummy = dummy.next
        return head