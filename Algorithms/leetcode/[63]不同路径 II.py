# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划

from copy import copy
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [1] + [0] * n
        # for i in range(m):
        #     for j in range(n):
        #         dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j-1] + dp[j]
        #
        # return dp[-2]

        # if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        #     return 0
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # state = [[0] * n for _ in range(m)]
        # ans = []
        # queue = []
        # def dfs(x, y):
        #     if x == m-1 and y == n-1:
        #         ans.append(queue[::])
        #         return
        #     if x < m-1 and obstacleGrid[x+1][y] == 0 and state[x+1][y] == 0:
        #         state[x+1][y] = 1
        #         queue.append([x+1, y])
        #         dfs(x+1, y)
        #         state[x+1][y] = 0
        #         queue.pop()
        #     if y < n-1 and obstacleGrid[x][y+1] == 0 and state[x][y+1] == 0:
        #         state[x][y+1] = 1
        #         queue.append([x, y+1])
        #         dfs(x, y+1)
        #         state[x][y+1] = 0
        #         queue.pop()
        # dfs(0, 0)
        # return len(ans)


        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

        
# leetcode submit region end(Prohibit modification and deletion)
