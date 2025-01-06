class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = Max = sum(nums[:k])
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]
            Max = Max if Max > curSum else curSum
        return Max/k