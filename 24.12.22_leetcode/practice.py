# 2024.12.22力扣网刷题
# 统计共同度过的日子数——数学、字符串——简单
# Alice 和 Bob 计划分别去罗马开会。
# 给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。
# 请你返回 Alice和 Bob 同时在罗马的天数。
# 你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。
# 示例 1：
# 输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# 输出：3
# 解释：Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。
# 示例 2：
# 输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# 输出：0
# 解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。
# 提示：
# 所有日期的格式均为 "MM-DD" 。
# Alice 和 Bob 的到达日期都 早于或等于 他们的离开日期。
# 题目测试用例所给出的日期均为 非闰年 的有效日期。

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arrive_month1, arrive_day1 = int(arriveAlice[0:2]), int(arriveAlice[3:5])
        arrive_month2, arrive_day2 = int(arriveBob[0:2]), int(arriveBob[3:5])
        leave_month1, leave_day1 = int(leaveAlice[0:2]), int(leaveAlice[3:5])
        leave_month2, leave_day2 = int(leaveBob[0:2]), int(leaveBob[3:5])
        # 确定在一起的日期
        begin_date = [0, 0]
        # 晚到的人为开始日期
        begin_date[0] = arrive_month1 if arrive_month1 > arrive_month2 else arrive_month2
        if arrive_month1 == arrive_month2:
            begin_date[1] = arrive_day1 if arrive_day1 > arrive_day2 else arrive_day2
        else:
            begin_date[1] = arrive_day1 if arrive_month1 > arrive_month2 else arrive_day2
        end_date = [0, 0]
        # 先走的人为结束日期
        end_date[0] = leave_month1 if leave_month1 < leave_month2 else leave_month2
        if leave_month1 == leave_month2:
            end_date[1] = leave_day1 if leave_day1 < leave_day2 else leave_day2
        else:
            end_date[1] = leave_day1 if leave_month1 < leave_month2 else leave_day2
        ans = 0
        for month in range(begin_date[0], end_date[0] + 1):
            if month == begin_date[0] == end_date[0]:
                ans += end_date[1] - begin_date[1] + 1
            elif month == begin_date[0]:
                ans += months[month] - begin_date[1] + 1
            elif month == end_date[0]:
                ans += end_date[1]
            else:
                ans += months[month]
        return ans if ans > 0 else 0



arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))

