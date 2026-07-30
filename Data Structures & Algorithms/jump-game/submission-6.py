class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r=0
        if len(nums)>1 and nums[0]==0:
            return False
        for l in range(len(nums)):
            if r<l:
                return False
            if l!=len(nums)-1 and nums[l]!=0:
                r=max(r,l+nums[l])
            
        return True
            
