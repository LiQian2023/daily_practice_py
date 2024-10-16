# 2024.10.16力扣网刷题
# 最小时间差——数组、数学、字符串、排序——中等
# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
# 示例 1：
# 输入：timePoints = ["23:59", "00:00"]
# 输出：1
# 示例 2：
# 输入：timePoints = ["00:00", "23:59", "00:00"]
# 输出：0
# 提示：
# 2 <= timePoints.length <= 2 * 10^4
# timePoints[i] 格式为 "HH:MM"


class Solution(object):
    def get_ans(self, h, m):
        if abs(h) >= 12 and m <= 0 or abs(h) >= 12 and m > 0 > h:
            h = 24 - abs(h)
        elif abs(h) >= 12 and m > 0:
            h = 24 - abs(h) - 1
        elif abs(h) < 12 and m < 0 and h <= 0:
            h = abs(h)
            m = abs(m)
        else:
            h = abs(h)
        return h * 60 + m
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        ans = []
        length = len(timePoints)
        for i in range(1, length + 1):
            if i == length:
                h = int(timePoints[0][:2]) - int(timePoints[i - 1][:2])
                m = int(timePoints[0][3:]) - int(timePoints[i - 1][3:])
            else:
                h = int(timePoints[i][:2]) - int(timePoints[i - 1][:2])
                m = int(timePoints[i][3:]) - int(timePoints[i - 1][3:])
            ans.append(self.get_ans(h, m))
        return min(ans)


# timePoints = ["00:00", "12:30", "13:00", "23:59", "22:20"]
timePoints = ["05:31","22:08","00:35"]
print(Solution().findMinDifference(timePoints))

