# 2025.05.03力扣网刷题
# 数组中的最大数对和——数组、哈希表——简单
# 给你一个下标从 0 开始的整数数组 nums 。请你从 nums 中找出和 最大 的一对数，且这两个数数位上最大的数字相等。
# 返回最大和，如果不存在满足题意的数字对，返回 - 1 。
# 示例 1：
# 输入：nums = [51, 71, 17, 24, 42]
# 输出：88
# 解释：
# i = 1 和 j = 2 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 71 + 17 = 88 。
# i = 3 和 j = 4 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 24 + 42 = 66 。
# 可以证明不存在其他数对满足数位上最大的数字相等，所以答案是 88 。
# 示例 2：
# 输入：nums = [1, 2, 3, 4]
# 输出： - 1
# 解释：不存在数对满足数位上最大的数字相等。
# 提示：
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Get_Max(num):
            ans = num % 10
            while num > 0:
                ans = max(ans, num % 10)
                num //= 10
            return ans
        def Count_Sort(nums):
            begin, end = nums[0], nums[0]
            for num in nums:
                if begin > num:
                    begin = num
                elif end < num:
                    end = num
            size = end - begin + 1
            hash = [0] * size
            for num in nums:
                key = num - begin
                hash[key] += 1
            ans = []
            for i in range(size - 1, -1, -1):
                while hash[i]:
                    ans.append(i + begin)
                    hash[i] -= 1
            return ans
        nums = Count_Sort(nums)
        hash = []
        size = [0] * 10
        for i in range(10):
            hash.append([])
        for num in nums:
            key = Get_Max(num)
            hash[key].append(num)
            size[key] += 1
        ans = -1
        for i in range(10):
            if size[i] > 1:
                tmp = hash[i][0] + hash[i][1]
                ans = max(ans, tmp)
        return ans
