class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1

        for i in range(1, (n+1)):
            one = dp[i-1]
            two = 0
            if i > 1:
                two = dp[i-2]
            dp[i] = one + two

        return dp[n] 
        # def fun(n, dp):
        #     if n == 0:
        #         return 1
        #     if dp[n] != -1:
        #         return dp[n]

        #     left = fun(n - 1, dp)
        #     right = 0
        #     if n > 1:
        #         right = fun(n - 2, dp)

        #     dp[n] = left + right
        #     return dp[n]

        # return fun(n, dp)