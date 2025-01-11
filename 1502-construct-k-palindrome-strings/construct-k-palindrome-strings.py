class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        dit = {}
        for i  in s:
            dit[i] = dit.get(i, 0) + 1
        count = 0
        for key,value in dit.items():
            if value % 2 == 1:
                count += 1
        if count > k: return False 
        return True