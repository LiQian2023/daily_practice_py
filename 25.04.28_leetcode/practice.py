# 2025.04.28力扣网刷题
# 出现最频繁的偶数元素——数组、哈希表、计数——简单
# 给你一个整数数组 nums ，返回出现最频繁的偶数元素。
# 如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 - 1 。
# 示例 1：
# 输入：nums = [0, 1, 2, 2, 4, 4, 1]
# 输出：2
# 解释：
# 数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
# 返回最小的那个，即返回 2 。
# 示例 2：
# 输入：nums = [4, 4, 4, 9, 2, 4]
# 输出：4
# 解释：4 是出现最频繁的偶数元素。
# 示例 3：
# 输入：nums = [29, 47, 21, 41, 13, 37, 25, 7]
# 输出： - 1
# 解释：不存在偶数元素。
# 提示：
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 10^5

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_, min_ = nums[0], nums[0]
        for num in nums:
            if num > max_:
                max_ = num
            elif num < min_:
                min_ = num
        size = max_ - min_ + 1
        hash = [0] * size
        for num in nums:
            key = num - min_
            hash[key] += 1
        ans = -1
        tmp = 0
        for i in range(size):
            key = i + min_
            if key % 2 == 0 and hash[i] > tmp:
                ans = key
                tmp = hash[i]
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 4, 4, 1]
    print(s.mostFrequentEven(nums))