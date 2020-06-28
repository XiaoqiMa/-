# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。 
# 
#  示例: 
# 
#  
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7
# ]] 
# 
#  说明: 
# 
#  
#  给定数组的长度不会超过15。 
#  数组中的整数范围是 [-100,100]。 
#  给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。 
#  
#  Related Topics 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(temp, ind, nums, res):
            if len(temp) >= 2:
                res.add(tuple(temp))
            used = set()
            for i in range(ind, len(nums)):
                if nums[i] in used:
                    continue
                if len(temp) == 0 or nums[i] >= temp[-1]:
                    used.add(nums[i])
                    temp.append(nums[i])
                    dfs(temp, i+1, nums, res)
                    temp.pop()
        res = set()
        dfs([], 0, nums, res)
        return list(res)

        # def dfs(num, temp):
        #     if len(temp) >= 2:
        #         res.append(temp)
        #     for i in range(len(num)):
        #         if len(temp)==0 or num[i] >= temp[-1]:
        #             dfs(num[i+1:], temp + [num[i]])
        #
        # res = []
        # dfs(nums, [])
        # ans = set()
        # for i in res:
        #     ans.add(tuple(i))
        # return list(ans)
        
# leetcode submit region end(Prohibit modification and deletion)
