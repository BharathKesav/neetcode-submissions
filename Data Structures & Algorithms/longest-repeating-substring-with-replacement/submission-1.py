class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        temp={}
        lar=0
        for r in range(len(s)):
            temp[s[r]]=1+temp.get(s[r],0)
            while sum(temp.values())-max(temp.values())>k:
                temp[s[l]]-=1
                l+=1
            lar=max(lar,sum(temp.values()))
        return lar            
