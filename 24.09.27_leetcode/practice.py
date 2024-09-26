# 2024.09.27力扣网刷题
# 合并区间——数组、排序——中等
# 以数组
# intervals表示若干个区间的集合，其中单个区间为intervals[i] = [starti, endi]。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 示例
# 1：
# 输入：intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出：[[1, 6], [8, 10], [15, 18]]
# 解释：区间[1, 3]和[2, 6]重叠, 将它们合并为[1, 6].
# 示例
# 2：
# 输入：intervals = [[1, 4], [4, 5]]
# 输出：[[1, 5]]
# 解释：区间[1, 4]和[4, 5]可被视为重叠区间。
# 提示：
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        length = len(intervals)
        for i in range(length-1):
            if intervals[i][0] <= intervals[i + 1][0] <= intervals[i][1]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i][0] = -1
                if intervals[i][1] > intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
                intervals[i][1] = -1
        i = 0
        while i < len(intervals):
            if intervals[i][0] == -1:
                intervals.pop(i)
            else:
                i += 1
        return intervals