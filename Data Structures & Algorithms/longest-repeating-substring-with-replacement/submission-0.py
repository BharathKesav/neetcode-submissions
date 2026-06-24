class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        temp={}
        lar=0
        for r in range(len(s)):
            temp[s[r]]=1+temp.get(s[r],0)
            while (r-l+1)-max(temp.values())>k:
                temp[s[l]]-=1
                l+=1
            lar=max(lar,r-l+1)
        return lar            
