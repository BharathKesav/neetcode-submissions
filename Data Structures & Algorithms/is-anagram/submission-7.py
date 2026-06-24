class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        for i in range(0,len(s)+len(t)):
            if i <len(s):    
                if s[i] in sd:
                    sd[s[i]]=sd[s[i]]+1
                else:
                    sd[s[i]]=1
            if i<len(t):
                if t[i] in td:
                    td[t[i]]=td[t[i]]+1
                else:
                    td[t[i]]=1
        if sd==td:
            return True
        else:
            return False