class Solution:
    def findCombination(self, index: int, arr: List[int], target: int, ans: List[List[int]], ds: List[int]) -> None:
        if (index == len(arr)):
            if(target == 0):
                ans.append(ds[:])
            return
        
        if(arr[index]) <= target:
            ds.append(arr[index])
            self.findCombination(index, arr, target - arr[index], ans, ds)
            ds.pop()
        self.findCombination(index + 1, arr, target, ans, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findCombination(0, candidates, target, ans, [])
        return ans