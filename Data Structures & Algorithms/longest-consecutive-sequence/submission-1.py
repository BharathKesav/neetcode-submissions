class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxlen=0
        curlen=0
        j=0
        for i in nums:
            curlen=0
            if i-1 not in nums:
                j=i
                
                while j in nums:
                    curlen+=1
                    j+=1
            if curlen>maxlen:
                maxlen=curlen
            
        return maxlen