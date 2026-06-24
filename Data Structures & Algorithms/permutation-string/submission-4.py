class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1=[0]*26
        a= False
        h2=[0]*26
        for i in s1:
            h1[ord(i)-ord('a')]+=1
        j=0
        for i in range(len(s2)):
            
            h2[ord(s2[i])-ord('a')]+=1
            if i-j+1>len(s1):
                
                h2[ord(s2[j])-ord('a')]-=1
                j+=1
            if h1==h2:
                a= True
        return a