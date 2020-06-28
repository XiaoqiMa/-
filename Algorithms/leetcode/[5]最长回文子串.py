# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ''
        for i in range(len(s)):
            temp = helper(s, i, i)
            if len(temp) > len(res):
                res = temp

            temp = helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp

        return res



        # if len(s) < 2:
        #     return s
        # max_len = 1
        # start = 0
        # dp = [[False] * len(s) for _ in range(len(s))]
        #
        # for i in range(len(s)):
        #     dp[i][i] = True
        #
        # for j in range(1, len(s)):
        #     for i in range(j):
        #         if s[i] == s[j]:
        #             if j - i < 3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
        #
        #         if dp[i][j]:
        #             curr_len = j - i + 1
        #             if curr_len >= max_len:
        #                 max_len = curr_len
        #                 start = i
        #
        # return s[start:start+max_len]



        
# leetcode submit region end(Prohibit modification and deletion)


