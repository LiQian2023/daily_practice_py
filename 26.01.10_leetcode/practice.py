# 2026.01.10力扣网刷题
# 3637. 三段式数组 I——数组、第461场周赛——简单
# 给你一个长度为 n 的整数数组 nums。
# 如果存在索引 0 < p < q < n − 1，使得数组满足以下条件，则称其为 三段式数组（trionic）：
# nums[0...p] 严格 递增，
# nums[p...q] 严格 递减，
# nums[q...n − 1] 严格 递增。
# 如果 nums 是三段式数组，返回 true；否则，返回 false。
# 示例 1:
# 输入: nums = [1, 3, 5, 4, 2, 6]
# 输出 : true
# 解释 :
# 选择 p = 2, q = 4：
# nums[0...2] = [1, 3, 5] 严格递增(1 < 3 < 5)。
# nums[2...4] = [5, 4, 2] 严格递减(5 > 4 > 2)。
# nums[4...5] = [2, 6] 严格递增(2 < 6)。
# 示例 2:
# 输入: nums = [2, 1, 3]
# 输出 : false
# 解释 :
# 无法选出能使数组满足三段式要求的 p 和 q 。
# 提示:
# 3 <= n <= 100
# - 1000 <= nums[i] <= 1000

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        flag = 1
        change = 0
        min_len = 0
        begin = 0
        for i in range(1, length):
            if flag == 1 and nums[i] < nums[i - 1]:
                change += 1
                flag = 0
                if min_len == 0 or i - begin < min_len:
                    min_len = i - begin
                begin = i - 1
            elif flag == 0 and nums[i] > nums[i - 1]:
                change += 1
                flag = 1
                if min_len == 0 or i - begin < min_len:
                    min_len = i - begin
                begin = i - 1
            elif nums[i] == nums[i - 1]:
                return False
        return change == 2 and min_len > 1