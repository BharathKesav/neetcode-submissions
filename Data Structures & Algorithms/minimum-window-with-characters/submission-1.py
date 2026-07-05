class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        have={}
        needcount=0
        for i in t:
            need[i]=1+need.get(i,0)
        needcount=len(need)
        a=[0,0]
        length=float('inf')
        l=0
        havcount=0
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]]=1+have.get(s[r],0)
                if have[s[r]]==need[s[r]]:
                    havcount+=1
            while havcount==needcount:
                if (r-l+1)<=length:
                    a=[l,r]
                    length=(r-l+1)
                if s[l] in have:
                    have[s[l]]-=1
                    if have[s[l]]<need[s[l]]:
                        havcount-=1
                l+=1
        return "" if length==float('inf') else s[a[0]:a[1]+1]



        


