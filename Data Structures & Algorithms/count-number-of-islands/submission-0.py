class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        cc = 0
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        stack=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0": continue
                if visited[i][j]: continue
                stack = [(i,j)]
                while stack:
                    node = stack.pop()
                    if visited[node[0]][node[1]]: continue
                    visited[node[0]][node[1]] = 1
                    for k in neighbours:
                        row = node[0]+k[0]
                        col = node[1]+k[1]
                        if row<0 or col<0: continue
                        if row>=len(grid) or col>=len(grid[0]): continue
                        if grid[row][col]!="1": continue
                        stack.append((row,col))
                cc+=1
        return cc


        