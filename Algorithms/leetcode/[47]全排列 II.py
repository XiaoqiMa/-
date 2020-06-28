# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], temp + [nums[i]])
        backtrack(nums, [])
        return res
        
# leetcode submit region end(Prohibit modification and deletion)