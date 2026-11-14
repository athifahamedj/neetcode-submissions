class Solution:
    # Input: prices = [10,1,5,6,7,1]
    # Output: 6
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0] 
        maxP = 0
        for r in range(len(prices)):
            if prices[r] < cheap :
                cheap = min(cheap, prices[r])
            maxP = max(maxP, prices[r]-cheap)
        return maxP
