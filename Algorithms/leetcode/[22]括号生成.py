# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。 
# 
#  例如，给出 n = 3，生成结果为： 
# 
#  [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # dp[i] = "(" + dp[j] + ")" + dp[i- j - 1]
        # if n == 0:
        #     return []
        #
        # dp = [None for _ in range(n + 1)]
        # dp[0] = [""]
        #
        # for i in range(1, n + 1):
        #     cur = []
        #     for j in range(i):
        #         left = dp[j]
        #         right = dp[i - j - 1]
        #         for s1 in left:
        #             for s2 in right:
        #                 cur.append("(" + s1 + ")" + s2)
        #     dp[i] = cur
        # return dp[n]


        ans = []

        def helper(left=n, right=n, temp=''):
            if left == 0 and right == 0:
                ans.append(temp)
                return
            if left < 0 or right < 0 or left > right:
                return
            helper(left-1, right, temp+'(')
            helper(left, right-1, temp+')')
        helper()
        return ans


        # ans = []
        #
        # def helper(left=0, right=0, temp=''):
        #     if len(temp) == 2 * n:
        #         ans.append(temp)
        #         return
        #     if left < n:
        #         helper(left + 1, right, temp + '(')
        #     if right < left:
        #         helper(left, right + 1, temp + ')')
        #
        # helper()
        # return ans

# leetcode submit region end(Prohibit modification and deletion)
