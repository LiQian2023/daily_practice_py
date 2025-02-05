# 2025.02.06力扣网刷题
# 转变日期格式——字符串——简单
# 给你一个字符串 date ，它的格式为 Day Month Year ，其中：
# Day 是集合{ "1st", "2nd", "3rd", "4th", ..., "30th", "31st" } 中的一个元素。
# Month 是集合{ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" } 中的一个元素。
# Year 的范围在 ​[1900, 2100] 之间。
# 请你将字符串转变为 YYYY - MM - DD 的格式，其中：
# YYYY 表示 4 位的年份。
# MM 表示 2 位的月份。
# DD 表示 2 位的天数。
# 示例 1：
# 输入：date = "20th Oct 2052"
# 输出："2052-10-20"
# 示例 2：
# 输入：date = "6th Jun 1933"
# 输出："1933-06-06"
# 示例 3：
# 输入：date = "26th May 1960"
# 输出："1960-05-26"
# 提示：
# 给定日期保证是合法的，所以不需要处理异常输入。

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        def helper(key):
            i = 1
            tmp = ['0', '0']
            while i >= 0:
                tmp[i] = str(key % 10)
                key //= 10
                i -= 1
            return ''.join(tmp)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        days = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
        my_list = date.split()
        ans = my_list[2]
        ans += '-'
        key = months.index(my_list[1]) + 1
        ans += helper(key)
        ans += '-'
        key = days.index(my_list[0]) + 1
        ans += helper(key)
        return ans
