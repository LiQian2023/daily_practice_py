# 2025.04.08力扣网刷题
# 使数组元素互不相同所需的最少操作次数——数组、哈希表——简单
# 给你一个整数数组 nums，你需要确保数组中的元素 互不相同 。为此，你可以执行以下操作任意次：
# 从数组的开头移除 3 个元素。如果数组中元素少于 3 个，则移除所有剩余元素。
# 注意：空数组也视作为数组元素互不相同。返回使数组元素互不相同所需的 最少操作次数 。
# 示例 1：
# 输入： nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
# 输出： 2
# 解释：
# 第一次操作：移除前 3 个元素，数组变为[4, 2, 3, 3, 5, 7]。
# 第二次操作：再次移除前 3 个元素，数组变为[3, 5, 7]，此时数组中的元素互不相同。
# 因此，答案是 2。
# 示例 2：
# 输入： nums = [4, 5, 6, 4, 4]
# 输出： 2
# 解释：
# 第一次操作：移除前 3 个元素，数组变为[4, 4]。
# 第二次操作：移除所有剩余元素，数组变为空。
# 因此，答案是 2。
# 示例 3：
# 输入： nums = [6, 7, 8, 9]
# 输出： 0
# 解释：
# 数组中的元素已经互不相同，因此不需要进行任何操作，答案是 0。
# 提示：
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, min_num = nums[0], nums[0]
        length = len(nums)
        for i in range(length):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[i])
        size = max_num - min_num + 1
        hash_table = []
        for i in range(size):
            hash_table.append([0, 0])
        ans = 0
        begin = 0
        i = 0
        while i < length:
            key = nums[i] - min_num
            if hash_table[key][0] == 0:
                hash_table[key][0] = 1
            else:
                if hash_table[key][1] >= begin:
                    mod = hash_table[key][1] % 3
                    delete = hash_table[key][1] + 3 - mod
                    ans = delete // 3
                    begin = delete
                    if begin > i:
                        i = begin - 1
            hash_table[key][1] = i
            i += 1
        return ans