class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i, num in zip(index, nums):
            output.insert(i, num)
        return output