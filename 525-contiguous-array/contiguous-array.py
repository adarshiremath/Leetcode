class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # if len(nums) == 2:
        #     if sum(nums) == 1:
        #         return 2
        #     else:
        #         return 0
        count = 0
        dit= {0:-1}
        Max = 0
        for i, x in enumerate(nums):
            count += 1 if x else -1
            # if x == 0:
            #     count -= 1
            # elif x == 1:
            #     count += 1
            if count in dit:
                Max = max(i - dit[count], Max)
            else:
                dit[count] = i
        
        return Max