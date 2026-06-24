class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=-1
        curr=0
        for i in range(len(prices)-1):
            curr=max(prices[i+1:])-prices[i]
            if curr>=maxprof:
                maxprof=curr
        if maxprof>0:
            return maxprof
        else:
            return 0