class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxx=-1
        while i<j:
            total=(j-i)*min(heights[i],heights[j])
            maxx=max(total,maxx)
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxx
