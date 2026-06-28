class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while j<=len(nums2)-1:
            arr.append(nums2[j])
            j+=1
        while i<=len(nums1)-1:
            arr.append(nums1[i])
            i+=1
        if len(arr)%2==0:
            x=arr[len(arr)//2]
            y=arr[(len(arr)//2)-1]
            return float((x+y)/2)
        else:
            x=arr[len(arr)//2]
            return float(x)
        