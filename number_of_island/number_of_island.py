class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        visited = [[False] * len(grid[0]) for x in range(len(grid))] # an 2d array that tracks which one are visited 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if not visited[x][y] and grid[x][y] == '1':
                    ans += 1
                    self.bfs(x, y, len(grid), len(grid[0]), visited, grid)
        return ans
    
    def bfs(self, x, y, x_max, y_max, visited, grid):
        queue = [(x,y)]
        while queue:
            top = queue.pop() # define the end of the list as the come out end of the queue, and the front of the list be the incoming end of the queue
            print(top)
            top_x = top[0]
            top_y = top[1]
            neighbours = [(top_x, top_y+1), (top_x+1, top_y), (top_x-1, top_y), (top_x, top_y-1)]
            for n in neighbours:
                if self.isValid(n, x_max, y_max) and not visited[n[0]][n[1]]:
                    visited[n[0]][n[1]] = True
                    if grid[n[0]][n[1]] == '1':
                        queue = [n] + queue
    
    def isValid(self, point, x_max, y_max):
        return point[0] >= 0 and point[0] <= x_max-1 and point[1] >= 0 and point[1] <= y_max-1
