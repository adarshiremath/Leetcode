class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        n = len(prices)
        for i in range(n):
            j = i+1
            while j < n:
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
                j += 1
            else:
                result.append(prices[i])
        return result