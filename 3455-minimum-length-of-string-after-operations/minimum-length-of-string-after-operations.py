class Solution:
    def minimumLength(self, s: str) -> int:
        dit = {}

        for i in s:
            dit[i] = dit.get(i, 0) + 1
        count = 0
        print(dit)
        for k, v in dit.items():
            temp = v
            while temp > 2:
                temp -= 2
            count += temp
        
        return count