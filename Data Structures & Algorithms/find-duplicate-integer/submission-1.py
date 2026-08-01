class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ass={}
        dup=0
        for i in nums:
            ass[i]=1+ass.get(i,0)
            if ass[i]>1:
                dup=i
                break
        return  dup