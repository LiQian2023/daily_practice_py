# 2025.05.23力扣网刷题
# 统计特殊四元组——数组、哈希表、枚举——简单
# 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组(a, b, c, d) 的 数目 ：
# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d
# 示例 1：
# 输入：nums = [1, 2, 3, 6]
# 输出：1
# 解释：满足要求的唯一一个四元组是(0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
# 示例 2：
# 输入：nums = [3, 3, 6, 4, 5]
# 输出：0
# 解释：[3, 3, 6, 4, 5] 中不存在满足要求的四元组。
# 示例 3：
# 输入：nums = [1, 1, 1, 3, 5]
# 输出：4
# 解释：满足要求的 4 个四元组如下：
# - (0, 1, 2, 3) : 1 + 1 + 1 == 3
# - (0, 1, 3, 4) : 1 + 1 + 3 == 5
# - (0, 2, 3, 4) : 1 + 1 + 3 == 5
# - (1, 2, 3, 4) : 1 + 1 + 3 == 5
# 提示：
# 4 <= nums.length <= 50
# 1 <= nums[i] <= 100

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        hash = {}
        for i in range(len_nums - 3):
            for j in range(i + 1, len_nums - 2):
                key = nums[i] + nums[j]
                if key in hash:
                    hash[key].append(j)
                else:
                    hash[key] = [j]
        ans = 0
        for i in range(2, len_nums - 1):
            for j in range(i + 1, len_nums):
                key = nums[j] - nums[i]
                if key in hash:
                    for k in hash[key]:
                        if k < i:
                            ans += 1
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3, 6]
    print(Solution().countQuadruplets(nums))


