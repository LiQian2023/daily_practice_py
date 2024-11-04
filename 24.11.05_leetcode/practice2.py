# 2024.11.05力扣网刷题
# 求出加密整数的和——数组、数学——简单
# 给你一个整数数组 nums ，数组中的元素都是 正 整数。
# 定义一个加密函数 encrypt ，encrypt(x) 将一个整数 x 中 每一个 数位都用 x 中的 最大 数位替换。比方说 encrypt(523) = 555 且 encrypt(213) = 333 。
# 请你返回数组中所有元素加密后的 和 。
# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：6
# 解释：加密后的元素位[1, 2, 3] 。加密元素的和为 1 + 2 + 3 == 6 。
# 示例 2：
# 输入：nums = [10, 21, 31]
# 输出：66
# 解释：加密后的元素为[11, 22, 33] 。加密元素的和为 11 + 22 + 33 == 66 。
# 提示：
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 1000

class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：数组
        length = len(nums)
        for i in range(length):
            m = nums[i] % 10
            n = 0
            while nums[i]:
                if nums[i] % 10 > m:
                    m = nums[i] % 10
                nums[i] /= 10
                n += 1
            while n:
                nums[i] *= 10
                nums[i] += m
                n -= 1
        return sum(nums)