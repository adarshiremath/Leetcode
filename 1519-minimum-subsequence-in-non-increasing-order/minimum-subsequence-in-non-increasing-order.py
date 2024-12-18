class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()
        i = n - 1
        while i > 0:
            if sum(nums[:i]) < sum(nums[i:]):
                return nums[i:][::-1]
            i -= 1
        return nums