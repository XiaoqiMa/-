# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新
# 的数据值留出空间。 
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # self.capacity = capacity
        # self.cache = {}
        # self.stack = []
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.tail.prev
        node.next = self.tail
        # order matters!!
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key not in self.cache:
        #     return -1
        # else:
        #     self.stack.remove(key)
        #     self.stack.append(key)
        #     return self.cache[key]
        if key in self.cache:
            self.move_to_tail(key)
        res = self.cache.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key in self.cache:
        #     self.cache[key] = value
        #     self.stack.remove(key)
        #     self.stack.append(key)
        # else:
        #     if len(self.cache) < self.capacity:
        #         self.cache[key] = value
        #         self.stack.append(key)
        #     else:
        #         k = self.stack.pop(0)
        #         self.stack.append(key)
        #         del self.cache[k]
        #         self.cache[key] = value

        if key in self.cache:
            self.cache[key].value = value
            self.move_to_tail(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.cache[key] = new
            new.next = self.tail
            new.prev = self.tail.prev
            self.tail.prev.next = new
            self.tail.prev = new





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
