class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sq(n):
            output = 0
            while n:
                temp = n % 10
                output += temp ** 2
                n = n // 10
            return output
        
        slow, fast = n, sum_sq(n)

        while slow != fast:
            fast = sum_sq(fast)
            fast = sum_sq(fast)
            slow = sum_sq(slow)
        return True if fast == 1 else False