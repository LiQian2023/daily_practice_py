# 2024.09.22力扣网刷题
# 找到小镇的法官——图、数组、哈希表——简单
# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
# 如果小镇法官真的存在，那么：
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 - 1 。
# 示例 1：
# 输入：n = 2, trust = [[1, 2]]
# 输出：2
# 示例 2：
# 输入：n = 3, trust = [[1, 3], [2, 3]]
# 输出：3
# 示例 3：
# 输入：n = 3, trust = [[1, 3], [2, 3], [3, 1]]
# 输出： - 1
# 提示：
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# trust 中的所有trust[i] = [ai, bi] 互不相同
# ai != bi
# 1 <= ai, bi <= n


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # 方法一：暴力求解
        length = len(trust)
        # 处理特殊情况
        if length == 0:
            if n == 1:
                return 1
            return -1
        i, j, ans = 0, 0, -1
        # 排序
        trust.sort(key=lambda x: x[1])\
        # 判断法官
        while i < length:
            # 记录村民人数
            count = 1
            for z in range(i+1, length):
                if trust[z][1] == trust[z - 1][1]:
                    count += 1
                    j += 1
                else:
                    break
            if count == n - 1:
                # 判断信任对象
                flag = True
                key = trust[i][1]
                for z in range(length):
                    if trust[z][0] == key:
                        flag = False
                        break
                if flag:
                    ans = trust[i][1]
                    break
            if count == 1:
                j += 1
            i = j
        return ans
