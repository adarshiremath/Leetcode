class Solution:
    def sumZero(self, n: int) -> List[int]:
        lis = [0] if n % 2 == 1 else []
        
        for i in range(1, (n//2) +1):
            lis.append(i)
            lis.append(-1 * i)
        
        return lis