class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        self.len = len(nums)
        
    def add(self, val: int) -> int:
        for i in range(self.len):
            if self.nums[i] > val: break
        else:
            i = self.len 
        self.nums = self.nums[: i] + [val] + self.nums[i :]
        self.len = len(self.nums)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)