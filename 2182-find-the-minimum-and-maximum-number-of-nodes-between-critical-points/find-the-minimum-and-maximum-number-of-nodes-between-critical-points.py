# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        dummy = head.next
        prev = head
        lis = []
        i = 1
        min1 = float('inf')
        while dummy and dummy.next:
            if (dummy.val > prev.val and dummy.val > dummy.next.val) or (dummy.val < prev.val and dummy.val < dummy.next.val):
                lis.append(i)
                if len(lis) > 1:
                    min1 = min(min1, lis[-1]-lis[-2])
            i += 1
            prev = dummy
            dummy = dummy.next
            
        if len(lis) > 1:
            max1 = lis[-1] - lis[0]
        else:
            return [-1, -1]
        return [min1, max1]
            
            
        