class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=nums[0]
        count=0
        for i in nums:
            if count<0:
                count=0
            count+=i
            summ=max(count,summ)
        return summ 