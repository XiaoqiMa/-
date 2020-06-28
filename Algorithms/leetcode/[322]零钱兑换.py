# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # memo = {0:0}
        # def backtrack(m):
        #     if m in memo:
        #         return memo[m]
        #     res = float('inf')
        #     for c in coins:
        #         if m >= c:
        #             res = min(res, backtrack(m - c) + 1)
        #     memo[m] = res
        #     return res
        # return backtrack(amount) if backtrack(amount) != float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1




        
# leetcode submit region end(Prohibit modification and deletion)
