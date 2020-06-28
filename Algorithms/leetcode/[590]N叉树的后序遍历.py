# 给定一个 N 叉树，返回其节点值的后序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其后序遍历: [5,6,3,2,4,1]. 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        unvisited, visited = 0, 1
        res = []
        stack = [(unvisited, root)]
        while stack:
            v, node = stack.pop()
            if node is None:
                continue
            if v == unvisited:
                stack.append((visited, node))
                for child in node.children[::-1]:
                    stack.append((unvisited, child))
            else:
                res.append(node.val)
        return res

        # if root is None:
        #     return []
        # res = []
        # for child in root.children:
        #     res += self.postorder(child)
        # res.append(root.val)
        # return res
        
# leetcode submit region end(Prohibit modification and deletion)
