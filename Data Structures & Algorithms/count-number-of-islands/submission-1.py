class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        nrows=len(grid)
        ncols=len(grid[0])
        visited=set()
        def bfs(row,col):
            queue=deque()
            visited.add((row,col))
            queue.append((row,col))
            
            while len(queue)>0:
                row,col=queue.pop()
                
                
                directions=[[0,-1],[0,1],[-1,0],[1,0]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r>=0 and r<len(grid)) and (c>=0 and c<len(grid[0])) and ((grid[r][c]=="1") and ((r,c) not in visited)):
                        queue.append((r,c))
                        visited.add((r,c))
        count=0
        for i in range(nrows):
            for j in range(ncols):
                if (grid[i][j]=="1" and ((i,j) not in visited ))  :
                    bfs(i,j)
                    count+=1
        return count


