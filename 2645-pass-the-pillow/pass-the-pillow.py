class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        i = 1
        t = 0
        while t < time:
            if direction == 1:
                if i < n:
                    i += 1
                else:
                    direction = -1
                    i -= 1
            else:
                if i > 1:
                    i -= 1
                else:
                    direction = 1
                    i += 1
            t += 1
        return i