class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>profit:
        #             profit=prices[j]-prices[i]
        # return profit
        # min_price = float('inf')
        # max_profit = 0
        
        # for price in prices:
        #     # Update minimum price seen so far
        #     if price < min_price:
        #         min_price = price
            
        #     # Calculate profit if we sell today
        #     profit = price - min_price
            
        #     # Update max profit
        #     if profit > max_profit:
        #         max_profit = profit

        # return max_profit

        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit