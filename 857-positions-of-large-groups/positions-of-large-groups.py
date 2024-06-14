class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        large = []
        left = 0
        right = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                right += 1
            else:
                if right - left >= 2:
                    large.append([left, right])
                left = i
                right = i
        if right - left >= 2:
            large.append([left, right])
        return sorted(large, key = lambda x: x[0])