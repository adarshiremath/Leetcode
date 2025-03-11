class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = {}
        
        def fun(ind):
            if ind < 0:
                return 0
            
            if ind in dp:
                return dp[ind]

            left = fun(ind - 1) + cost[ind]
            right = float("inf")
            if ind > 0:
                right = fun(ind - 2) + cost[ind]
            
            dp[ind] = min(left, right)
            return dp[ind]
        
        return min(fun(n-1), fun(n-2))