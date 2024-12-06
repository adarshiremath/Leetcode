class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set()
        
        for ban in banned:
            if ban < n+1:
                banned_set.add(ban)
        totSum = 0
        count = 0
        for num in range(1, n+1):
            if num not in banned_set:
                totSum += num
                if totSum <= maxSum:
                    count += 1
                else:
                    break
        return count