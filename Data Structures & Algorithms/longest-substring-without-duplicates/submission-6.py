class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        i=0
        curr=0
        maxx=0
        for j in range(len(s)):
            while s[j] in se:
                se.remove(s[i])
                i+=1
            se.add(s[j])
            curr=j-i+1
            maxx=max(curr,maxx)
        return maxx
