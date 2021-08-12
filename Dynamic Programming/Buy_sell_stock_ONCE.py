def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i]-minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
            
        return maxProfit
