from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        One-pass algorithm:
        • Track the lowest price seen so far (min_price).
        • For each day’s price, compute the potential profit if we sold today
          (price - min_price) and keep the best seen.
        """
        min_price = float('inf')   # +∞  – no price seen yet
        max_profit = 0             # best profit so far

        for price in prices:
            if price < min_price:
                min_price = price            # found a new cheaper buying day
            else:
                # possible profit if we buy at min_price and sell today
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
