class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1

        for i in range(1, (n+1)):
            one = prev
            two = 0
            if i > 1:
                two = prev2
            cur = one + two
            prev2 = prev
            prev = cur

        return prev
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