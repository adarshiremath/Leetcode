class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,element in enumerate(nums):
            remain = target - element

            if remain in seen:
                return [i, seen[remain]]
            
            seen[element] = i
        