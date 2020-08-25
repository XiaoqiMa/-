# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。 
# 
#  例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
#  2, 5]。 
# 
#  对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。 
# 
#  那么成功对给定单词列表进行编码的最小字符串长度是多少呢？ 
# 
#  
# 
#  示例： 
# 
#  输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 2000 
#  1 <= words[i].length <= 7 
#  每个单词都是小写字母 。 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.word_end = True

    def start_with(self, prefix):
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, reverse=True, key=len)
        count = 0
        trie = Trie()
        for word in words:
            if not trie.start_with(word[::-1]):
                count += len(word) + 1
                trie.insert(word[::-1])
        return count


        
# leetcode submit region end(Prohibit modification and deletion)
