class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = sorted(list(set(arr)))
        arr_dit = {}
        for i in range(len(arr_set)):
            arr_dit[arr_set[i]] = i + 1
        output = []
        
        for i in arr:
            output.append(arr_dit[i])
        
        return output