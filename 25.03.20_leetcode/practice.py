# 2025.03.20力扣网刷题
# 找到字符串中合法的相邻数字——哈希表、字符串、计数——简单
# 给你一个只包含数字的字符串 s 。如果 s 中两个 相邻 的数字满足以下条件，我们称它们是 合法的 ：
# 前面的数字 不等于 第二个数字。
# 两个数字在 s 中出现的次数 恰好 分别等于这个数字本身。
# 请你从左到右遍历字符串 s ，并返回最先找到的 合法 相邻数字。如果这样的相邻数字不存在，请你返回一个空字符串。
# 示例 1：
# 输入：s = "2523533"
# 输出："23"
# 解释：
# 数字 '2' 出现 2 次，数字 '3' 出现 3 次。"23" 中每个数字在 s 中出现的次数都恰好分别等于数字本身。所以输出 "23" 。
# 示例 2：
# 输入：s = "221"
# 输出："21"
# 解释：
# 数字 '2' 出现 2 次，数字 '1' 出现 1 次。所以输出 "21" 。
# 示例 3：
# 输入：s = "22"
# 输出：""
# 解释：
# 没有合法的相邻数字。
# 提示：
# 2 <= s.length <= 100
# s 只包含 '1' 到 '9' 的数字。

class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        def GetAns(num_list, s, i, ans):
            key1, key2 = int(s[i]), int(s[i + 1])
            if num_list[key1] == key1 and num_list[key2] == key2:
                ans = s[i] + s[i + 1]
                return ans, True
            return ans, False
        len1 = len(s)
        num_list = [0] * 10
        for i in range(len1):
            key = int(s[i])
            num_list[key] += 1
        ans = ""
        for i in range(len1 - 1):
            if s[i] != s[i + 1]:
                if i:
                    ans, flag = GetAns(num_list, s, i, ans)
                    if flag:
                        break
                else:
                    ans, flag = GetAns(num_list, s, i, ans)
                    if flag:
                        break
        return ans

if __name__ == '__main__':
    s = "2523533"
    print(Solution().findValidPair(s))