class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_, max_ = 1, max(nums)
        n =len(nums)

        while min_ < max_:
            mid = (min_ + max_) //2
            index = 0
            theft = 0

            while index < n:
                if nums[index] <= mid:
                    index += 2
                    theft += 1
                else:
                    index += 1
                
            if theft >= k:
                max_ = mid
            else:
                min_ = mid + 1
        return min_