class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            digit_sums[i] = digit_sums[i // 10] + i % 10
        freq = [0] * 37
        for i in range(1, n + 1):
            freq[digit_sums[i]] += 1
        
        max_freq = max(freq)
        return freq.count(max_freq)