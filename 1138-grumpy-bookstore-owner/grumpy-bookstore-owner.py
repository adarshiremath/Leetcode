class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxv = 0
        count = 0
        for customer, is_grumpy in zip(customers, grumpy):
            if is_grumpy == 0:
                count += customer
        for i in range(0, len(customers)-minutes+1):
            p = 0
            for j in range(i, i+minutes):
                if grumpy[j] == 1:
                    p += customers[j]
            maxv = max(maxv, count+p)
        return maxv