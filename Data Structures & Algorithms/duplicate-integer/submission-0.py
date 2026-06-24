class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=False
        for i in range(0,len(nums)-1):
            count=i+1
            while(count<=len(nums)-1):
                if(nums[i]==nums[count]):
                    a= True
                count+=1
        return a

        