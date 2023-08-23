class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = {}
        for i in nums: dit[i] = dit.get(i, 0) + 1
        lis = []
        for key, v in dit.items():
            lis.append([key, v])
        lis = list(zip(*sorted(lis, key=lambda x: x[1], reverse =True)))
        return lis[0][:k]