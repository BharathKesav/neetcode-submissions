class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        arr=[]
        for r in range(len(nums)):
            if r-l+1>=k:
                arr.append(max(nums[l:r+1]))
                l+=1
        return arr