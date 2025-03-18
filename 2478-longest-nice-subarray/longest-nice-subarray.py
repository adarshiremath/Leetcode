class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        max_len = 0
        while r < len(nums):
            # If the bitwise AND of the current subarray is non-zero, include nums[r] in the subarray
            if ans & nums[r] == 0:
                ans |= nums[r]  # Add nums[r] to the subarray
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                # If not, move the left pointer to the right
                ans ^= nums[l]  # Remove nums[l] from the subarray
                l += 1
        return max_len
