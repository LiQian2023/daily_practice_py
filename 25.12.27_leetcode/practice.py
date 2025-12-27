# 2025.12.27力扣网刷题
# 3386. 按下时间最长的按钮——数组、第428场周赛——简单
# 给你一个二维数组 events，表示孩子在键盘上按下一系列按钮触发的按钮事件。
# 每个 events[i] = [indexi, timei] 表示在时间 timei 时，按下了下标为 indexi 的按钮。
# 数组按照 time 的递增顺序排序。
# 按下一个按钮所需的时间是连续两次按钮按下的时间差。按下第一个按钮所需的时间就是其时间戳。
# 返回按下时间 最长 的按钮的 index。如果有多个按钮的按下时间相同，则返回 index 最小的按钮。
# 示例 1：
# 输入： events = [[1, 2], [2, 5], [3, 9], [1, 15]]
# 输出： 1
# 解释：
# 下标为 1 的按钮在时间 2 被按下。
# 下标为 2 的按钮在时间 5 被按下，因此按下时间为 5 - 2 = 3。
# 下标为 3 的按钮在时间 9 被按下，因此按下时间为 9 - 5 = 4。
# 下标为 1 的按钮再次在时间 15 被按下，因此按下时间为 15 - 9 = 6。
# 最终，下标为 1 的按钮按下时间最长，为 6。
# 示例 2：
# 输入： events = [[10, 5], [1, 7]]
# 输出： 10
# 解释：
# 下标为 10 的按钮在时间 5 被按下。
# 下标为 1 的按钮在时间 7 被按下，因此按下时间为 7 - 5 = 2。
# 最终，下标为 10 的按钮按下时间最长，为 5。
# 提示：
# 1 <= events.length <= 1000
# events[i] == [indexi, timei]
# 1 <= indexi, timei <= 10^5
# 输入保证数组 events 按照 timei 的递增顺序排序。

class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        cord = [events[0][0], events[0][1]]
        maxtime = events[0][1]
        for event in events[1:]:
            if event[1] - cord[1] >= maxtime:
                if (event[0] < cord[0] and event[1] - cord[1] == maxtime) or (event[1] - cord[1] > maxtime):
                    cord[0] = event[0]
                maxtime = event[1] - cord[1]
            cord[1] = event[1]
        return cord[0]