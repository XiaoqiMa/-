# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root] if root else []
        ans = []
        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return ans

        # queue = collections.deque([root])
        # ans = []
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node:
        #             level.append(node.val)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if level:
        #         ans.append(level)
        # return ans
# leetcode submit region end(Prohibit modification and deletion)
