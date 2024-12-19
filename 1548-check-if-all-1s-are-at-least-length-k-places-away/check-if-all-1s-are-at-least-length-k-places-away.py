class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -float('inf')
        for i, num in enumerate(nums):
            if num == 1:
                if i - last > k:
                    last = i
                else:
                    return False
        return True