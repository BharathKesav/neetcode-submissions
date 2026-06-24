class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in range(k):
            max_key=max(d,key=d.get)
            li.append(max_key)
            d.pop(max_key)
        return li
