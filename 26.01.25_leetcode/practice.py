# 26.01.25力扣网刷题
# LCR 172. 统计目标成绩的出现次数h——数组、二分查找——简单
# 某班级考试成绩按非严格递增顺序记录于整数数组 scores，请返回目标成绩 target 的出现次数。
# 示例 1：
# 输入 : scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4
# 输出 : 3
# 示例 2：
# 输入 : scores = [1, 2, 3, 5, 7, 9], target = 6
# 输出 : 0
# 提示：
# 0 <= scores.length <= 10^5
# - 10^9 <= scores[i] <= 10^9
# scores 是一个非递减数组
# - 10^9 <= target <= 10^9
# 注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        # 方法一：二分查找
        length = len(scores)
        l, r = 0, length - 1
        # 找左边界
        while l <= r:
            m = l + (r - l) // 2
            if scores[m] < target:
                l = m + 1
            else:
                r = m - 1
        left = r + 1
        l, r = 0, length - 1
        while l <= r:
            m = l + (r - l) // 2
            if scores[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return l - left
