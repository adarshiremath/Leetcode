class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dit = {}
        l = 0
        max_ = 0

        for r in range(0, len(s)):
            if s[r] in dit:
                l = max(l, dit[s[r]]+1)
            dit[s[r]] = r
            max_ = max(max_, r - l + 1)
        
        return max_