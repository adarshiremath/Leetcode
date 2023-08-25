class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findVal(low, high):
            if len(nums[low:high]) == 1:
                if nums[low:high][0] == target:
                    return low
                return -1
            else:
                mid = (high + low) // 2
                l = findVal(low, mid)
                r = findVal(mid, high)
                return l if l > r else r
        return findVal(0, len(nums))