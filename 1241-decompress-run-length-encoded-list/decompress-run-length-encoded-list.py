class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)//2
        arr = []
        for i in range(n):
            freq, val = nums[2*i], nums[2*i + 1]
            arr += [val]*freq
        return arr