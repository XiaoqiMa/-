# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = [root] if root else []
        ans = []
        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]

        return ans

        # if root is None:
        #     return []
        # queue = collections.deque([root])
        # ans = []
        # while queue:
        #     res = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         res.append(node.val)
        #         queue.extend(node.children)
        #     ans.append(res)
        # return ans

        
# leetcode submit region end(Prohibit modification and deletion)
