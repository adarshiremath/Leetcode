class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dit = {}
        res = 0 
        for i, x in enumerate(s):
            if x in dit:
                dit[x][-1] = i
            else:
                dit[x] = [i, i]
        
        for k, (first, last) in dit.items():
            if last > first + 1:
                res += len(set(s[first+1:last]))
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dit = {}
        # res = set()
        # for i, x in enumerate(s):
        #     if x not in dit:
        #         dit[x] = i
        #     else:
        #         if i - dit[x] > 1:
        #             for j in range(dit[x]+1, i):
        #                 res.add(x + s[j] + x)
        # return len(res)