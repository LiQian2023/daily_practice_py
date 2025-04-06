# 2025.04.07力扣网刷题
# 独一无二的出现次数——数组、哈希表——简单
# 给你一个整数数组 arr，如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
# 示例 1：
# 输入：arr = [1, 2, 2, 1, 1, 3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
# 示例 2：
# 输入：arr = [1, 2]
# 输出：false
# 示例 3：
# 输入：arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# 输出：true
# 提示：
# 1 <= arr.length <= 1000
# - 1000 <= arr[i] <= 1000

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        len1 = len(arr)
        max_num, min_num = arr[0], arr[0]
        for i in range(1, len1):
            if arr[i] < min_num:
                min_num = arr[i]
            if arr[i] > max_num:
                max_num = arr[i]
        len2 = max_num - min_num + 1
        hash1 = [0] * len2
        max_num = 0
        for i in range(len1):
            key = arr[i] - min_num
            hash1[key] += 1
            if hash1[key] > max_num:
                max_num = hash1[key]
        hash2 = [0] * (max_num + 1)
        for i in range(len2):
            if hash1[i]:
                key = hash1[i]
                hash2[key] += 1
                if hash2[key] > 1:
                    return False
        return True

if __name__ == '__main__':

