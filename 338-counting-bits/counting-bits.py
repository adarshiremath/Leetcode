class Solution:
    def countBits(self, n: int) -> List[int]:
        dic = {}
        for i in range(n+1):
            dic[i] = bin(i)
        count = []
        for key, value in dic.items():
            count.append(int(str(value).count('1')))
        return count