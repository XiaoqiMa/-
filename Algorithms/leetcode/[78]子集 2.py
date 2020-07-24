# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        # def backtrack(i, temp):
        #     res.append(temp)
        #     for j in range(i, len(nums)):
        #         backtrack(j+1, temp + [nums[j]])
        #
        # backtrack(0, [])
        # return res

        def backtrack(nums, temp):
            ans.append(temp)
            for i in range(len(nums)):
                backtrack(nums[i+1:], temp + [nums[i]])

        ans = []
        backtrack(nums, [])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
