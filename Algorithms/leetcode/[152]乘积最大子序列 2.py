# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。 
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_min = cur_max = ans = nums[0]
        for num in nums[1:]:
            cur_max, cur_min = max(cur_max * num, cur_min * num, num), \
                               min(cur_max * num, cur_min * num, num)
            ans = max(ans, cur_max)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
