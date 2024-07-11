class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # dit = {'b':0, 'a':0, 'n':0, 'l':0, 'o':0}
        # for i in text:
        #     if i in dit.keys():
        #         dit[i] += 1
        # count = min(dit['b'], dit['a'], dit['n'], dit['l']//2, dit['o']//2)
        # return count
        
        b, a, n, l, o = 0, 0, 0, 0, 0
        
        for i in text:
            if i == 'b':
                b += 1
            elif i == 'a':
                a += 1
            elif i == 'n':
                n += 1
            elif i == 'l':
                l += 1
            elif i == 'o':
                o += 1
        return min(b, a, n, l//2, o//2)