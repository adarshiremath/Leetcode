class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        dit= {0:-1}
        Max = 0
        for i, x in enumerate(nums):
            count += 1 if x else -1
            if count in dit:
                Max = i - dit[count] if i - dit[count] > Max else Max
            else:
                dit[count] = i
        return Max