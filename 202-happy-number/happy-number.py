class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digit_sq(digits: str):
            sum_sq = 0
            for digit in digits:
                digit = int(digit)
                sum_sq += (digit)**2
            return sum_sq
        
        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = get_digit_sq(str(n))
        return False