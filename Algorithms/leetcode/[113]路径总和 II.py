# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def helper(root, sum, temp):
            if not root:
                return
            if not root.left and not root.right and sum - root.val == 0:
                ans.append(temp + [root.val])
                return
            helper(root.left, sum-root.val, temp+[root.val])
            helper(root.right, sum-root.val, temp+[root.val])

        if not root:
            return []
        ans = []
        helper(root, sum, [])
        return ans


        # if not root:
        #     return []
        # stack = [([root.val], root)]
        # res = []
        # while stack:
        #     tmp, node = stack.pop()
        #     if not node.right and not node.left and sum(tmp) == sum_:
        #         res.append(tmp)
        #     if node.right:
        #         stack.append((tmp + [node.right.val], node.right))
        #     if node.left:
        #         stack.append((tmp + [node.left.val], node.left))
        # return res


# leetcode submit region end(Prohibit modification and deletion)
