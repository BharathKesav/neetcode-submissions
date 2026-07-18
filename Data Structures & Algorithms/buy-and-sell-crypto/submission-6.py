class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=float('-inf')
        buy=0
        sell=1
        while buy<sell and sell<len(prices):
            prof=max(prof,prices[sell]-prices[buy])
            if prices[buy]>prices[sell]:
                buy=sell
                sell+=1
            else:
                sell+=1
        if prof<0:
            return 0
        else:
            return prof
            
