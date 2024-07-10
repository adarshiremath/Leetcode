class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lis = text.split(" ")
        res = []
        for i in range(2, len(lis)):
            if lis[i-2] == first and lis[i-1] == second:
                res.append(lis[i])
        return res