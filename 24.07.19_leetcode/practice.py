# 2024.07.19力扣网刷题
# 清除数字——哈希表、字符串、模拟——简单
# 给你一个字符串 s 。
# 你的任务是重复以下操作删除 所有 数字字符：
# 删除 第一个数字字符 以及它左边 最近 的 非数字 字符。
# 请你返回删除所有数字字符以后剩下的字符串。
# 示例 1：
# 输入：s = "abc"
# 输出："abc"
# 解释：
# 字符串中没有数字。
# 示例 2：
# 输入：s = "cb34"
# 输出：""
# 解释：
# 一开始，我们对 s[2] 执行操作，s 变为 "c4" 。
# 然后对 s[1] 执行操作，s 变为 "" 。
# 提示：
# 1 <= s.length <= 100
# s 只包含小写英文字母和数字字符。
# 输入保证所有数字都可以按以上操作被删除。


class Solution(object):
    def clearDigits1(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s_len = len(s)
        i = 0
        while i < s_len:
            if s[i].isdigit():
                s.pop(i)
                s.pop(i - 1)
                s_len -= 2
                i -= 1
            else:
                i += 1
        return ''.join(s)

    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i in s:
            if i.isdigit():
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)


s = 'cb34'
print(Solution().clearDigits(s))