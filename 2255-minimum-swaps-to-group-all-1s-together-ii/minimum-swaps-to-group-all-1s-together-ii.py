class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        minimum_swaps = float("inf")
        total_ones = sum(nums)
        ones_count = nums[0]
        end = 0
        for start in range(len(nums)):
            if start != 0:
                ones_count -= nums[start - 1]
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)
        return minimum_swaps