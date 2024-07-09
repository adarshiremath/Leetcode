class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait, done = 0, 0
        for arrivel, time in customers:
            done = max(arrivel, done) + time
            wait += done - arrivel
        print(wait)
        return wait/len(customers)