# 编写一个算法来判断一个数是不是“快乐数”。 
# 
#  一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
# 如果可以变为 1，那么这个数就是快乐数。 
# 
#  示例: 
# 
#  输入: 19
# 输出: true
# 解释: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
#  Related Topics 哈希表 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def f(m):
            sum_ = 0
            while m > 0:
                sum_ += (m % 10) ** 2
                m = m // 10
            return sum_

        slow = f(n)
        fast = f(f(n))
        while slow != fast:
            slow = f(slow)
            fast = f(f(fast))
        return slow == 1
# leetcode submit region end(Prohibit modification and deletion)