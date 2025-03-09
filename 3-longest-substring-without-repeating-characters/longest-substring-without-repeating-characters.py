class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dit = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in dit:
                l = max(dit[s[r]]+1, l)
            dit[s[r]] = r
            res = max(res, r - l + 1)
        return res