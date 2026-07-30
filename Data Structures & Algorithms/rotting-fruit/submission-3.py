class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=collections.deque()
        fresh,time=0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))

        while fresh>0 and queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()     
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row>=0 and row<len(grid)) and (col>=0 and col<len(grid[0])) and (grid[row][col]==1):
                        grid[row][col]=2
                        queue.append((row,col))
                        fresh-=1
            time+=1
        if fresh==0:
            return time
        else:
            return -1
