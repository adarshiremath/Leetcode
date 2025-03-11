class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev = nums[0]
        prev2 = 0
        for n in range(1, len(nums)):
            left = nums[n]
            if n > 1:
                left += prev2
            right = 0 + prev

            cur = max(left, right)
            prev2 = prev
            prev = cur

        return prev

        # dp = [-1] * len(nums)
        # dp[0] = nums[0]

        # for n in range(1, len(nums)):
        #     left = 0
        #     if n > 1:
        #         left = nums[n] + dp[n - 2]
        #     right = 0 + dp[n - 1]

        #     dp[n] = max(left, right)

        # return dp[len(nums)-1]
        # def fun(n):
        #     if n == 0:
        #         return nums[0]
        #     if n < 0:
        #         return 0
        #     if dp[n] != -1:
        #         return dp[n]

        #     left = nums[n] + fun(n - 2)
        #     right = 0 + fun(n - 1)

        #     dp[n] = max(left, right)

        #     return dp[n]

        # return fun(len(nums) - 1)