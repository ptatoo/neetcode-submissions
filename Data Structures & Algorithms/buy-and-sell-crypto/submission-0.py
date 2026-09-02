class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = prices[0]

        for n in prices:
            if n <= minPrice:
                minPrice = n
            else:
                result = max(result, n - minPrice)

        return result