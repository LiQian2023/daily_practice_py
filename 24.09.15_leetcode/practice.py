# 2024.09.15力扣网刷题
# 与车相交的点——数组、哈希表、前缀和——简单
# 给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。
# 对于任意下标 i，nums[i] = [starti, endi] ，其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。
# 返回数轴上被车 任意部分 覆盖的整数点的数目。
# 示例 1：
# 输入：nums = [[3, 6], [1, 5], [4, 7]]
# 输出：7
# 解释：从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。
# 示例 2：
# 输入：nums = [[1, 3], [5, 8]]
# 输出：7
# 解释：1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。
# 提示：
# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100

class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        # 方法一：排序+合并区间+求和
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1][0] <= nums[i][0] <= nums[i - 1][1]:
                nums[i][0] = nums[i - 1][0]
                nums[i - 1][0] = 0
                if nums[i][1] < nums[i - 1][1]:
                    nums[i][1] = nums[i - 1][1]
                nums[i - 1][1] = 0
        ans = 0
        for i in range(0, len(nums)):
            if nums[i][0] == 0:
                continue
            ans += nums[i][1] - nums[i][0] + 1
        return ans


nums = [[1,5],[6,9],[1,4],[6,8]]
print(Solution().numberOfPoints(nums))