class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lis = [0]*(len(s)+1)
        for start, end, direction in shifts:
            side = direction if direction == 1 else -1
            lis[start] += side
            lis[end+1] -= side
        preSum = 0
        res = ""
        for j, c in enumerate(s):
            preSum += lis[j]
            res += chr(97 + ((ord(c) - 97 + preSum) % 26))
        return res