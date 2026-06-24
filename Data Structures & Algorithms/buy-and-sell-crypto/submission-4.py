class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=float('-inf')
        curr=0
        b=0
        s=1
        while s<len(prices):
            if prices[s]-prices[b]>maxprof:
                maxprof=prices[s]-prices[b]
            if prices[s]<prices[b]:
                b=s
                s+=1
            else:
                s+=1
        if maxprof<=0:
            return 0
        else:
            return maxprof
