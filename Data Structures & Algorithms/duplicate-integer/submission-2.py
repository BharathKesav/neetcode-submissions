class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        a=False
        for i in range(0,len(nums)):
            if nums[i] in d:
                a=True
            else:
                d[nums[i]]=i
        return a

        