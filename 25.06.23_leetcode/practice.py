# 2025.06.23力扣网刷题
# 检查元素频次是否为质数——数组、哈希表、数学、计数、概论——简单
# 给你一个整数数组 nums。
# 如果数组中任一元素的 频次 是 质数，返回 true；否则，返回 false。
# 元素 x 的 频次 是它在数组中出现的次数。
# 质数是一个大于 1 的自然数，并且只有两个因数：1 和它本身。
# 示例 1：
# 输入： nums = [1, 2, 3, 4, 5, 4]
# 输出： true
# 解释：
# 数字 4 的频次是 2，而 2 是质数。
# 示例 2：
# 输入： nums = [1, 2, 3, 4, 5]
# 输出： false
# 解释：
# 所有元素的频次都是 1。
# 示例 3：
# 输入： nums = [2, 2, 2, 4, 4]
# 输出： true
# 解释：
# 数字 2 和 4 的频次都是质数。
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def Isprime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            if n == 1:
                return False
            return True
        my_set = set(nums)
        my_hash = {}
        for i in my_set:
            my_hash[i] = nums.count(i)
        for i in my_hash:
            if Isprime(my_hash[i]):
                return True
        return False