class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        dit = {}
        for i in s:
            dit[i] = dit.get(i, 0) + 1
        init = 97
        while dit:
            while init < 123:
                if chr(init) in dit:
                    res += chr(init)
                    dit[chr(init)] -= 1
                    if dit[chr(init)] == 0:
                        del dit[chr(init)]
                init += 1
            
            while init > 96:
                if chr(init) in dit:
                    res += chr(init)
                    dit[chr(init)] -= 1
                    if dit[chr(init)] == 0:
                        del dit[chr(init)]
                init -= 1
        return res