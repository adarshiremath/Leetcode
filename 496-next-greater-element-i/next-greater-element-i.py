class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dit = [], {}
        for num in nums2:
            while stack and num > stack[-1]:
                dit[stack.pop()] = num
            stack.append(num)
        while stack:
            dit[stack.pop()] = -1
        result = []
        for num in nums1:
            result.append(dit.get(num, -1))
        return result