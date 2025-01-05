class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cumnums = []
        Sum = 0
        for x in nums:
            Sum += x
            self.cumnums.append(Sum)
        print(self.cumnums)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.cumnums[right] - self.cumnums[left -1] if left > 0 else self.cumnums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)