# 2025.02.17力扣网刷题
# 有序数组中出现次数超过25 % 的元素——数组——简单
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25 % 。
# 请你找到并返回这个整数
# 示例：
# 输入：arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
# 输出：6
# 提示：
# 1 <= arr.length <= 10 ^ 4
# 0 <= arr[i] <= 10 ^ 5

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        key = length * 0.25
        tmp = 1
        for i in range(1, length):
            if arr[i] == arr[i-1]:
                tmp += 1
                if tmp > key:
                    return arr[i]
            else:
                tmp = 1
        return arr[0]