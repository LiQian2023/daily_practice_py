# 2026.03.14力扣网刷题
# 3692. 众数频率字符——中级工程师、第166场双周赛——简单
# 给你一个由小写英文字母组成的字符串 s。
# 对于一个值 k，频率组 是在 s 中恰好出现 k 次的字符集合。
# 众数频率组 是包含 不同 字符数量最多的频率组。
# 返回一个字符串，包含众数频率组中的所有字符，字符的顺序 不限 。如果两个或多个频率组的大小并列最大，则选择其频率 k 较大 的那个组。
# 示例 1:
# 输入: s = "aaabbbccdddde"
# 输出 : "ab"
# 解释 :
# 频率(k)	组中不同字符	组大小	是否众数 ?
# 4	{d}	1	否
# 3	{a, b}	2	是
# 2	{c}	1	否
# 1	{e}	1	否
# 字符 'a' 和 'b' 的频率相同，都为 3，它们在众数频率组中。
# 示例 2:
# 输入: s = "abcd"
# 输出 : "abcd"
# 解释 :
# 频率(k)	组中不同字符	组大小	是否众数 ?
# 1	{a, b, c, d}	4	是
# 所有字符的频率都相同，都为 1，它们都在众数频率组中。
# 示例 3 :
# 输入 : s = "pfpfgi"
# 输出 : "fp"
# 解释 :
# 频率(k)	组中不同字符	组大小	是否众数 ?
# 2	{p, f}	2	是
# 1	{g, i}	2	否(组大小并列，选择频率更大的 k = 2)
# 字符 'p' 和 'f' 的频率相同，都为 2，它们在众数频率组中。频率为 1 的组大小并列，但我们选择频率更高的组 2。
# 提示:
# 1 <= s.length <= 100
# s 只包含小写英文字母。

class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash1 = {}
        hash2 = {}
        for c in s:
            if c not in hash1:
                hash1[c] = 1
            else:
                hash1[c] += 1
        for key in hash1:
            if hash1[key] not in hash2:
                hash2[hash1[key]] = 1
            else:
                hash2[hash1[key]] += 1
        target, count = 0, 0
        for key in hash2:
            if hash2[key] >= count:
                target = key
                count = hash2[key]
        ans = ''
        for key in hash1:
            if hash1[key] == target:
                ans += key
        return ans