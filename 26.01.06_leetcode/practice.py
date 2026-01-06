# 2026.01.06力扣网刷题
# 3718. 缺失的最小倍数——数组、哈希表、第427场周赛——简单
# 给你一个整数数组 nums 和一个整数 k，请返回从 nums 中缺失的、最小的正整数 k 的倍数。
# 倍数 指能被 k 整除的任意正整数。
# 示例 1：
# 输入： nums = [8, 2, 3, 4, 6], k = 2
# 输出： 10
# 解释：
# 当 k = 2 时，其倍数为 2、4、6、8、10、12……，其中在 nums 中缺失的最小倍数是 10。
# 示例 2：
# 输入： nums = [1, 4, 7, 10, 15], k = 5
# 输出： 5
# 解释：
# 当 k = 5 时，其倍数为 5、10、15、20……，其中在 nums 中缺失的最小倍数是 5。
# 提示：
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100

class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
        ans, i = 0, 1
        while 1:
            if k * i not in hash:
                ans = k * i
                break
            i += 1
        return ans