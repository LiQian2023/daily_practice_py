# 2024.11.24力扣网刷题
# 点名——位运算、数组、哈希表、数学、二分查找——简单
# 某班级 n 位同学的学号为 0 ~n - 1。点名结果记录于升序数组 records。假定仅有一位同学缺席，请返回他的学号。
# 示例 1:
# 输入: records = [0, 1, 2, 3, 5]
# 输出 : 4
# 示例 2 :
# 输入 : records = [0, 1, 2, 3, 4, 5, 6, 8]
# 输出 : 7
# 提示：
# 1 <= records.length <= 10000

class Solution(object):
    # 方法一：数组
    def takeAttendance1(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        i = 0
        length = len(records)
        while i < length:
            if records[i] != i:
                break
            i += 1
        return i
    # 方法二：数学
    def takeAttendance2(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        length = len(records)
        ans = length * (length + 1) // 2
        for i in range(length):
            ans -= records[i]
        return ans
    # 方法三：位运算
    def takeAttendance3(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        i = 0
        length = len(records)
        while i < length:
            records[i] ^= i
            if records[i]:
                break
            i += 1
        return i
    # 方法四：哈希表
    def takeAttendance4(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        length = len(records)
        hash = [0] * (length + 1)
        for i in range(length):
            hash[records[i]] += 1
        ans = 0
        while ans < length + 1:
            if hash[ans] == 0:
                break
            ans += 1
        return ans
    # 方法五：二分查找
    def takeAttendance(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        length = len(records)
        l, r = 0, length - 1
        while l <= r:
            m = (l + r) // 2
            if records[m] == m:
                l = m + 1
            else:
                r = m - 1
        return l