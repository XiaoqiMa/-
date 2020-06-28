# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false. 
#  Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        state = [[0] * n for _ in range(m)]
        def dfs(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or state[i][j] or board[i][j] != word[ind]:
                return False
            state[i][j] = 1
            for x, y in directions:
                if dfs(i+x, j+y, ind+1):
                    return True
            state[i][j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False






# leetcode submit region end(Prohibit modification and deletion)
