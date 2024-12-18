from typing import List


class Solution:
    """
    Brute force solution
    """

    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n):
            discount = 0
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            prices[i] = prices[i] - discount
        return prices


class Solution:
    """
    Optimized solution using monotonic stack
    """

    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices
