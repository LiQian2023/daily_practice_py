# 2025.04.02力扣网刷题
# 有序三元组中的最大值 I——数组——简单
# 给你一个下标从 0 开始的整数数组 nums 。
# 请你从所有满足 i < j < k 的下标三元组(i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。
# 下标三元组(i, j, k) 的值等于(nums[i] - nums[j]) * nums[k] 。
# 示例 1：
# 输入：nums = [12, 6, 1, 2, 7]
# 输出：77
# 解释：下标三元组(0, 2, 4) 的值是(nums[0] - nums[2]) * nums[4] = 77 。
# 可以证明不存在值大于 77 的有序下标三元组。
# 示例 2：
# 输入：nums = [1, 10, 3, 4, 19]
# 输出：133
# 解释：下标三元组(1, 2, 4) 的值是(nums[1] - nums[2]) * nums[4] = 133 。
# 可以证明不存在值大于 133 的有序下标三元组。
# 示例 3：
# 输入：nums = [1, 2, 3]
# 输出：0
# 解释：唯一的下标三元组(0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
# 提示：
# 3 <= nums.length <= 100
# 1 <= nums[i] <= 10^6

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_i = 0
        _len = len(nums)
        for i in range(_len):
            if nums[i] > nums[max_i]:
                max_i = i
        left = [0, 0]
        if max_i >= 2:
            for i in range(max_i):
                for j in range(i + 1, max_i):
                    if (nums[i] - nums[j]) > (nums[left[0]] - nums[left[1]]):
                        left = [i, j]
        right = [-1, -1]
        if max_i < _len - 2:
            for i in range(max_i + 1, _len - 1):
                tmp = right[::]
                if tmp[0] == -1 or nums[i] < nums[tmp[0]]:
                    tmp[0] = i
                    for j in range(i + 1, _len):
                        if tmp[1] <= tmp[0] or nums[j] > nums[tmp[1]]:
                            tmp[1] = j
                if right[0] == -1 or (nums[max_i] - nums[tmp[0]]) * nums[tmp[1]] > (nums[max_i] - nums[right[0]]) * nums[right[1]]:
                    right = tmp[::]
        # 无右侧
        if max_i >= _len - 2:
            if nums[left[0]] - nums[left[1]] > 0:
                return (nums[left[0]] - nums[left[1]]) * nums[max_i]
            return 0
        # 无左侧
        if max_i < 2:
            if right[0] != -1:
                return (nums[max_i] - nums[right[0]]) * nums[right[1]]
            return 0
        # 两侧都有
        tmp1 = (nums[left[0]] - nums[left[1]]) * nums[max_i]
        tmp2 = (nums[max_i] - nums[right[0]]) * nums[right[1]]
        return tmp1 if tmp1 > tmp2 else tmp2