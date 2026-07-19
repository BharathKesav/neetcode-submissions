class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for l in range(len(temperatures)):
            r=l+1
            while r<len(temperatures):
                if temperatures[r]>temperatures[l]:
                    res.append(r-l)
                    break
                elif (r==len(temperatures)-1 and temperatures[r]<=temperatures[l]):
                    res.append(0)
                r+=1
            if l==len(temperatures)-1:
                res.append(0)
        return res

            