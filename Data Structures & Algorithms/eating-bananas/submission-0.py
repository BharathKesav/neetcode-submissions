class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        def hoursate(mid):
            totalhours=0
            for g in piles:
                totalhours+=math.ceil(g/mid)
            return totalhours
        while i<j:
            mid=(i+j)//2
            if hoursate(mid)<=h:
                j=mid
            else:
                i=mid+1
        return i
        



