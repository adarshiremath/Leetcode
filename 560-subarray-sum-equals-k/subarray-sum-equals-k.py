class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        dit = {0:1}
        count = 0
        Sum = []
        for i, x in enumerate(nums):
            preSum += x
            if preSum - k in dit:
                count += dit[preSum - k]
            dit[preSum] = dit.get(preSum, 0) + 1
        return count