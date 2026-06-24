class Solution:
    def trap(self, height: List[int]) -> int:
        maxl=-1
        maxr=-1
        water=0
        for i in range(1,len(height)-1):
            maxl=max(height[:i])
            maxr=max(height[i+1:])
            if maxl<height[i] or maxr<height[i]:
                continue
            else:
                water+=min(maxl,maxr)-height[i]
                print(maxl,maxr)
            maxl=0
            maxr=0
        return water
