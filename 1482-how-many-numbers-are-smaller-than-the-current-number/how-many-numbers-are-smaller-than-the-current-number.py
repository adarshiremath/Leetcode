class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dit = {}
        res = []
        for i, num in enumerate(sorted_nums):
            if num not in dit:
                dit[num] = i
        for num in nums:
            res.append(dit[num])
        return res