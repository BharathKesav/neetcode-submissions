class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count=0
        while count<len(matrix) and target>matrix[count][len(matrix[count])-1]:
            count+=1
        if count==len(matrix):
            return False

        i=0
        j=len(matrix[count])-1
        while i<=j and j<len(matrix[count]):
            mid=(i+j)//2
            if target==matrix[count][mid]:
                return True
            elif target<matrix[count][mid]:
                j=mid-1
            else:
                i=mid+1
        return False
