class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0]*38
        arr[0], arr[1], arr[2], i = 0, 1, 1, 3
        if n < 3: return arr[n]
        while i != n+1:
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
            i += 1
        return arr[n]