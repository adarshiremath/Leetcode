class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = []
        
        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                return i
    