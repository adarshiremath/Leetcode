class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        
        for i in nums:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        j, k = 0, 0
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = e[j]
                j += 1
            else:
                nums[i] = o[k]
                k += 1
        return nums