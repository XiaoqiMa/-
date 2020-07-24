# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。 
# 
#  示例 1: 
# 
#  
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释: 
# 长度最长的公共子数组是 [3, 2, 1]。
#  
# 
#  说明: 
# 
#  
#  1 <= len(A), len(B) <= 1000 
#  0 <= A[i], B[i] < 100 
#  
#  Related Topics 数组 哈希表 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])

        return res
        
# leetcode submit region end(Prohibit modification and deletion)
