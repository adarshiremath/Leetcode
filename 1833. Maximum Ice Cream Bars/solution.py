class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs = sorted(costs)
        i = 0
        count = 0
        remain = coins
        while(i < len(costs)-1):
            if remain >= costs[i]:
                remain -= costs[i]
                count += 1
            if remain < costs[i+1]:
                return count
            i += 1
        if remain >= costs[-1]:
            return count + 1
        return count
