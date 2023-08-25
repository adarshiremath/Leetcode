class Solution:
    def findMin(self, nums: List[int]) -> int:
        def minVal(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                length = len(nums)
                l = minVal(nums[:length//2])
                r = minVal(nums[length//2:])
                return l if l < r else r
        return minVal(nums)