class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count_T, window = {}, {} 

        for c in t:
            count_T[c] = count_T.get(c, 0) + 1
        
        have, need = 0, len(count_T)

        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count_T and window[s[r]] == count_T[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else "" 