# 2025.05.11力扣网刷题
# 存在连续三个奇数的数组——数组——简单
# 给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。
# 示例 1：
# 输入：arr = [2, 6, 4, 1]
# 输出：false
# 解释：不存在连续三个元素都是奇数的情况。
# 示例 2：
# 输入：arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
# 输出：true
# 解释：存在连续三个元素都是奇数的情况，即[5, 7, 23] 。
# 提示：
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)
        i = 1
        while i < length - 1:
            a = arr[i - 1] % 2
            b = arr[i] % 2
            c = arr[i + 1] % 2
            if a and b and c:
                return True
            if b == 0 and c:
                i += 1
            elif c == 0:
                i += 2
            i += 1
        return False