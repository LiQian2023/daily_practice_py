# 2025.07.30力扣网刷题
# 检查二进制字符串字段——字符串、第231场周赛——简单
# 给你一个二进制字符串 s ，该字符串 不含前导零 。
# 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
# 示例 1：
# 输入：s = "1001"
# 输出：false
# 解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
# 示例 2：
# 输入：s = "110"
# 输出：true
# 提示：
# 1 <= s.length <= 100
# s[i] 为 '0' 或 '1'
# s[0] 为 '1'

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(1, length):
            if s[i] == '1' and s[i-1] == '0':
                return False
        return True

