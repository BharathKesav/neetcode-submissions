class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxscore=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxscore=max(maxscore,height * (i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            maxscore=max(maxscore,h*(len(heights)-i))
        return maxscore 