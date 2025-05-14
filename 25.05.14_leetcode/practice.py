# 2025.05.14力扣网刷题
# 移除最小数对使数组有序 I——数组、哈希表、链表、双向链表、有序集合、模拟、堆（优先队列）——简单
# 给你一个数组 nums，你可以执行以下操作任意次数：
# 选择 相邻 元素对中 和最小 的一对。如果存在多个这样的对，选择最左边的一个。
# 用它们的和替换这对元素。
# 返回将数组变为 非递减 所需的 最小操作次数 。
# 如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为非递减。
# 示例 1：
# 输入： nums = [5, 2, 3, 1]
# 输出： 2
# 解释：
# 元素对(3, 1) 的和最小，为 4。替换后 nums = [5, 2, 4]。
# 元素对(2, 4) 的和为 6。替换后 nums = [5, 6]。
# 数组 nums 在两次操作后变为非递减。
# 示例 2：
# 输入： nums = [1, 2, 2]
# 输出： 0
# 解释：
# 数组 nums 已经是非递减的。
# 提示：
# 1 <= nums.length <= 50
# - 1000 <= nums[i] <= 1000

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Is_non_decreasing(nums, length):
            for i in range(length - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        def Hash_Record(nums, size):
            hash = [0] * size
            for i in range(size):
                hash[i] = nums[i] + nums[i + 1]
            return hash
        def Delete(hash, key, nums, length):
            for i in range(size):
                if hash[i] == key:
                    nums[i] = hash[i]
                    for j in range(i + 1, size):
                        nums[j] = nums[j + 1]
                    length -= 1
                    break
            return nums, length
        length = len(nums)
        ans = 0
        flag = False
        while not flag:
            flag = Is_non_decreasing(nums, length)
            if not flag:
                size = length - 1
                hash = Hash_Record(nums, size)
                key = min(hash)
                nums, length = Delete(hash, key, nums, length)
                ans += 1
        return ans