# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设
# 网格的四个边均被水包围。 
# 
#  示例 1: 
# 
#  输入:
# 11110
# 11010
# 11000
# 00000
# 
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# 11000
# 11000
# 00100
# 00011
# 
# 输出: 3
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # def dfs(i, j):
        #     grid[i][j] = '0'
        #     for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        #         new_x = x + i
        #         new_y = y + j
        #         if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
        #             dfs(new_x, new_y)
        #
        # if not grid:
        #     return 0
        # m = len(grid)
        # n = len(grid[0])
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             count += 1
        #             dfs(i, j)
        # return count

        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0

        def bfs(i, j):
            queue = collections.deque()
            queue.appendleft((i, j))
            grid[i][j] = '0'
            while queue:
                i, j = queue.pop()
                for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    new_x = x + i
                    new_y = y + j
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '0'
                        queue.appendleft((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        return count

9# leetcode submit region end(Prohibit modification and deletion)