class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree(root, nums, i):
    if i < len(nums):
        if nums[i] == '#':
            return None
        else:
            root = TreeNode(nums[i])
            root.left = create_tree(root.left, nums, 2 * i + 1)
            root.right = create_tree(root.right, nums, 2 * i + 2)
            return root  # !!important to return root node
    return root


def pre_order(root):
    if root is None:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)


def in_order(root):
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


def in_order2(root):
    if root:
        yield from in_order2(root.left)
        yield root.val
        yield from in_order2(root.right)

def post_order(root):
    if root is None:
        return
    visited, unvisited = 1, 0
    stack = [(unvisited, root)]

    while stack:
        state, node = stack.pop()
        if node:
            if state == unvisited:
                stack.append((visited, node))
                stack.append((unvisited, node.right))
                stack.append((unvisited, node.left))
            if state == visited:
                ans.append(node.val)

nums = [1, 2, 3, 4, "#", '#', 5, 6]
root = create_tree(None, nums, 0)
print(in_order(root))
print(pre_order(root))

nums2 = [4, 2, 6, 1, 3, 5, 7]
node = create_tree(None, nums2, 0)
print(list(in_order2(node)))

ans = []
num3 = [1, 2, 3, 4, 5, 6]
node3 = create_tree(None, num3, 0)
post_order(node3)
print(ans)