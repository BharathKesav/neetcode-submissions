class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dummy=[1]*len(nums)
        prod=1
        for i in range(1,len(nums)):
            prod=prod*nums[i-1]
            dummy[i]=prod
        prod=1
        for j in range(len(nums)-2,-1,-1):
            prod=prod*nums[j+1]
            dummy[j]=dummy[j]*prod
        return dummy

