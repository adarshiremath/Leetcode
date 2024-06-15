class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        m = -1
        while n:
            if 1&n:
                if m==-1:
                    m = 1
                else:
                    ans = max(ans,m)
                    m=1
            else:
                if m!=-1:
                    m+=1
                
            n = n>>1
        
        return ans