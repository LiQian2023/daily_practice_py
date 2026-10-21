# 2026.10.21力扣网刷题
# 3863. 将一个字符串排序的最小操作次数——资深工程师、字符串、第492场周赛——重点
# 给你一个由小写英文字母组成的字符串 s。
# 在一次操作中，你可以选择 s 的任意 子字符串（但 不能 是整个字符串），并将其按 非降序字母顺序 进行 排序。
# 返回使 s 按 非降序 排列所需的 最小 操作次数。如果无法做到，则返回 - 1。
# 示例 1：
# 输入： s = "dog"
# 输出： 1
# 解释：
# 将子字符串 "og" 排序为 "go"。
# 现在，s = "dgo"，已按升序排列。因此，答案是 1。
# 示例 2：
# 输入： s = "card"
# 输出： 2
# 解释：
# 将子字符串 "car" 排序为 "acr"，得到 s = "acrd"。
# 将子字符串 "rd" 排序为 "dr"，得到 s = "acdr"，已按升序排列。因此，答案是 2。
# 示例 3：
# 输入： s = "gf"
# 输出： - 1
# 解释：
# 在给定提示下，无法对 s 进行排序。因此，答案是 - 1。
# 提示：
# 1 <= s.length <= 10^5
# s 仅由小写英文字母组成。

class Solution:
    def minOperations(self, s: str) -> int:
        hash, n = [0] * 26, len(s)
        if n == 2:
            if s[0] > s[1]:
                return -1
            return 0
        
        for ch in s:
            hash[ord(ch) - ord('a')] += 1
        tmp = []
        for i in range(26):
            while hash[i]:
                tmp.append(chr(i + ord('a')))
                hash[i] -= 1
        ans = 0
        for i in range(n):
            if s[i] != tmp[i]:
                ans = 1
                break
        if ans:
            if s[0] != tmp[0] and s[-1] != tmp[-1]:
                l, r = 1, 1
                for i in range(n):
                    if 0 <= i < n - 1 and s[i] == tmp[0]:
                        l = 0
                        break
                    elif 1 <= i < n and s[i] == tmp[-1]:
                        r = 0
                        break
                ans += l + r
        return ans