# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # top-down
        # if not triangle:
        #     return
        # for i in range(1, len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             triangle[i][j] += triangle[i-1][j]
        #         elif j == len(triangle[i]) - 1:
        #             triangle[i][j] += triangle[i-1][j-1]
        #         else:
        #             triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        # return min(triangle[-1])


        # bottom-up
        if not triangle:
            return
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

        
# leetcode submit region end(Prohibit modification and deletion)


