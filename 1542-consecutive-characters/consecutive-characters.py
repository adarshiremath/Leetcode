class Solution:
    def maxPower(self, s: str) -> int:
        s_pow = [1]
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                s_pow.append(s_pow[i-1] + 1)
            else:
                s_pow.append(1)
        return max(s_pow)