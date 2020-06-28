# 给定一个没有重复数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], temp+[nums[i]])
        res = []
        backtrack(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
