# 2025.03.10力扣网刷题
# 删除字符使频率相同——哈希表、字符串、计数——简单
# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
# 注意：
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。
# 示例 1：
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母：word 变成 "abc" 且每个字母出现频率都为 1 。
# 示例 2：
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
# 提示：
# 2 <= word.length <= 100
# word 只包含小写英文字母。

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        hash = {}
        for ch in word:
            if ch in hash:
                hash[ch] += 1
            else:
                hash[ch] = 1
        min_count, max_count = hash[word[0]], hash[word[0]]
        for key in hash:
            if hash[key] > max_count:
                max_count = hash[key]
            elif hash[key] < min_count:
                min_count = hash[key]
        counts = [0, 0]
        for key in hash:
            if hash[key] == min_count:
                counts[0] += 1
            elif hash[key] == max_count:
                counts[1] += 1
        if counts[1] * max_count == length - 1:
            return True
        elif counts[0] * min_count + min_count == length - 1:
            return True
        elif counts[1] == 0 and (counts[0] == 1 or min_count == 1):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    word = "aazz"
    print(s.equalFrequency(word))