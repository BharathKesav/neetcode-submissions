class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dect={}
        final=[]
        
        for i in strs:
            temp=[0]*26
            for j in i:
                temp[ord(j)-ord('a')]+=1
            if tuple(temp) in dect:
                dect[tuple(temp)]=dect[tuple(temp)]+[i]
            else:
                dect[tuple(temp)]=[i]
        for key in dect:
            final.append(dect[key])
        return final
