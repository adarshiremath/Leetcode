class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        Set = set()
        
        for i in range(len(arr)):
            if (2 * arr[i] in Set) or (arr[i] % 2 == 0 and arr[i] / 2 in Set):
                return True
            Set.add(arr[i])
        return False