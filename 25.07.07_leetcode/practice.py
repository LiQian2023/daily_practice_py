# 2025.07.07力扣网刷题
# 删除字符串中的所有相邻重复项——栈、字符串——简单
# 给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 s 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
# 示例：
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
# 之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
# 提示：
# 1 <= s.length <= 10^5
# s 仅由小写英文字母组成。

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        length = len(res)
        i = 1
        while i < length:
            if i and res[i] == res[i-1]:
                res.pop(i)
                res.pop(i-1)
                length -= 2
                i -= 1
            else:
                i += 1
        return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("abbaca"))