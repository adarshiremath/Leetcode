class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = ''
        for i in bin(n)[2:]:
            if i == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)