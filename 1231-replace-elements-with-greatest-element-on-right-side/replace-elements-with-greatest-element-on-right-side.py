class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max = arr[-1]
        arr[-1] = -1
        i = len(arr)-2
        while i > -1:
        # for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = Max
            if temp > Max: Max = temp
            i -= 1
        return arr