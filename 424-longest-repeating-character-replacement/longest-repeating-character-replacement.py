class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dit = {}
        result = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            dit[s[r]] = dit.get(s[r], 0) + 1
            maxf = max(maxf, dit[s[r]])

            if (r - l + 1) - maxf > k:
                dit[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result