# 2025.02.13力扣网刷题
# 验证外星语词典——数组、哈希表、字符串——简单
# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
# 示例 1：
# 输入：words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# 输出：true
# 解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
# 示例 2：
# 输入：words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
# 输出：false
# 解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
# 示例 3：
# 输入：words = ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
# 输出：false
# 解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# 在 words[i] 和 order 中的所有字符都是英文小写字母。

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        len1, len2 = len(words), len(order)
        hash = [0] * 26
        i = 0
        while i < len2:
            key = ord(order[i]) - ord('a')
            hash[key] = i
            i += 1
        for i in range(len1 - 1):
            size1, size2 = len(words[i]), len(words[i + 1])
            j = 0
            while j < size1 and j < size2:
                key1, key2 = ord(words[i][j]) - ord('a'), ord(words[i + 1][j]) - ord('a')
                if hash[key1] > hash[key2]:
                    return False
                elif hash[key1] < hash[key2]:
                    break
                j += 1
            if j == size1 or j == size2:
                if size1 > size2:
                    return False
        return True
