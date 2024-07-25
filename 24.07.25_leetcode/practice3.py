# 2024.07.25力扣网刷题
# 最长和谐子序列——数组、哈希、计数、排序、滑动窗口
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
# 示例 1：
# 输入：nums = [1, 3, 2, 2, 5, 2, 3, 7]
# 输出：5
# 解释：最长的和谐子序列是[3, 2, 2, 2, 3]
# 示例 2：
# 输入：nums = [1, 2, 3, 4]
# 输出：2
# 示例 3：
# 输入：nums = [1, 1, 1, 1]
# 输出：0
# 提示：
# 1 <= nums.length <= 2 * 10^4
# - 10^9 <= nums[i] <= 10^9

class Solution(object):
    def findLHS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_nums = len(nums)
        i, j = 0, 0
        m = 0
        count = 0
        while i < len_nums and j < len_nums:
            if nums[j] - nums[i] == 1:
                count = j - i + 1
                j += 1
            elif nums[j] - nums[i] == 2:
                i += 1
            elif nums[j] - nums[i] == 0:
                j += 1
            else:
                i = j
            if count > m:
                m = count
            count = 0
        if count > m:
            m = count
        return m

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        ans = [nums_dict[i] + nums_dict[i + 1] for i in nums_dict if i + 1 in nums_dict ]
        return max(ans) if ans else 0


nums = [1,1,4,4,5]
print(Solution().findLHS(nums))
