class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        rows,cols=len(grid),len(grid[0])
        visited=set()
        maxx=0
        def bfs(r,c)->int:
            tempp=1
            queue=collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                row,col=queue.popleft()
                directions=[[-1,0],[1,0],[0,-1],[0,1]] #top,down,left,right
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c]==1) and ((r,c) not in visited):
                        visited.add((r,c))
                        queue.append((r,c))
                        tempp+=1 
            return tempp
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    temp=bfs(r,c)
                    maxx=max(temp,maxx)
        return  maxx

