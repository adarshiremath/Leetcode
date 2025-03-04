class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate(ind, nums):
            if ind == len(nums):
                res.append(nums[:])
                return  
            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                generate(ind+1,nums)
                nums[i], nums[ind] = nums[ind], nums[i]
        
        generate(0, nums)
        return res
