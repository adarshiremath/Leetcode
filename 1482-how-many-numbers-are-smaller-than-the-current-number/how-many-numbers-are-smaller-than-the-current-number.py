class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            val = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        val += 1
            res.append(val)
        
        return res