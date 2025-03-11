class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * 46

        def fun(n, dp):
            if n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]

            left = fun(n - 1, dp)
            right = 0
            if n > 1:
                right = fun(n - 2, dp)

            dp[n] = left + right
            return dp[n]
            
        return fun(n, dp)