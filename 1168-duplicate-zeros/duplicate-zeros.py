class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = arr
        n = len(arr)
        i = 0 
        while i < n:
            if temp[i] == 0:
                temp = temp[:i] + [0] + temp[i:n-1]
                i += 1
            i += 1
            
        for i in range(len(arr)):
            arr[i] = temp[i]