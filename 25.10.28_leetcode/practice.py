# 2025.10.28力扣网刷题
# 使数组元素等于零——数组、前缀和、模拟、第424场周赛——简单
# 给你一个整数数组 nums 。
# 开始时，选择一个满足 nums[curr] == 0 的起始位置 curr ，并选择一个移动 方向 ：向左或者向右。
# 此后，你需要重复下面的过程：
# 如果 curr 超过范围[0, n - 1] ，过程结束。
# 如果 nums[curr] == 0 ，沿当前方向继续移动：如果向右移，则 递增 curr ；如果向左移，则 递减 curr 。
# 如果 nums[curr] > 0:
# 将 nums[curr] 减 1 。
# 反转 移动方向（向左变向右，反之亦然）。
# 沿新方向移动一步。
# 如果在结束整个过程后，nums 中的所有元素都变为 0 ，则认为选出的初始位置和移动方向 有效 。
# 返回可能的有效选择方案数目。
# 示例 1：
# 输入：nums = [1, 0, 2, 0, 3]
# 输出：2
# 解释：
# 可能的有效选择方案如下：
# 选择 curr = 3 并向左移动。
# [1, 0, 2, 0, 3] ->[1, 0, 2, 0, 3] ->[1, 0, 1, 0, 3] ->[1, 0, 1, 0, 3] ->[1, 0, 1, 0, 2] ->[1, 0, 1, 0, 2] ->[1, 0, 0, 0, 2] ->[1, 0, 0, 0, 2] ->[1, 0, 0, 0, 1] ->[1, 0, 0, 0, 1] ->[1, 0, 0, 0, 1] ->[1, 0, 0, 0, 1] ->[0, 0, 0, 0, 1] ->[0, 0, 0, 0, 1] ->[0, 0, 0, 0, 1] ->[0, 0, 0, 0, 1] ->[0, 0, 0, 0, 0].
# 选择 curr = 3 并向右移动。
# [1, 0, 2, 0, 3] ->[1, 0, 2, 0, 3] ->[1, 0, 2, 0, 2] ->[1, 0, 2, 0, 2] ->[1, 0, 1, 0, 2] ->[1, 0, 1, 0, 2] ->[1, 0, 1, 0, 1] ->[1, 0, 1, 0, 1] ->[1, 0, 0, 0, 1] ->[1, 0, 0, 0, 1] ->[1, 0, 0, 0, 0] ->[1, 0, 0, 0, 0] ->[1, 0, 0, 0, 0] ->[1, 0, 0, 0, 0] ->[0, 0, 0, 0, 0].
# 示例 2：
# 输入：nums = [2, 3, 4, 0, 4, 1, 0]
# 输出：0
# 解释：
# 不存在有效的选择方案。
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# 至少存在一个元素 i 满足 nums[i] == 0 。

class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        zero = []
        zero_num = 0
        # 记录 cur 的个数与起始位置
        for i in range(length):
            if nums[i] == 0:
                zero.append(i)
                zero_num += 1
        def Move(nums, cur, length, dic):
            while 0 <= cur < length:
                if nums[cur] > 0:
                    nums[cur] -= 1
                    dic *= -1
                cur += dic
            for num in nums:
                if num != 0:
                    return 0
            return 1
        ans = 0
        for i in range(zero_num):
            # 左移
            ans += Move(nums[::], zero[i], length, -1)
            # 右移
            ans += Move(nums[::], zero[i], length, 1)
        return ans

    def countValidSelections1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suffix = sum(nums)
        ans, prefix = 0, 0
        for num in nums:
            if num:
                prefix += num
            elif suffix == prefix * 2:
                ans += 2
            elif abs(prefix * 2 - suffix) == 1:
                ans += 1
        return ans