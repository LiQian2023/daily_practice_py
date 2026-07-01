# 2026.07.01力扣网刷题
# 14. 最长公共前缀——字典树、数组、字符串——简单
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1：
# 输入：strs = ["flower", "flow", "flight"]
# 输出："fl"
# 示例 2：
# 输入：strs = ["dog", "racecar", "car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 提示：
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 如果非空，则仅由小写英文字母组成
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len1 = len(strs[0])
        size = len1
        for i in range(1, len(strs)):
            len2 = len(strs[i])
            j = 0
            while j < len1 and j < len2:
                if strs[i][j] != strs[0][j]:
                    break
                else:
                    j += 1
            size = min(size, j)
        return strs[0][:size]