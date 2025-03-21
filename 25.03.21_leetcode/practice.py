# 2025.03.21力扣网刷题
# 最小展台数量——数组、哈希表、字符串、计数——简单
# 力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。
# 已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， demand[i][j] 表示第 i 天展览时第 j 个展台的类型。
# 在满足每一天展台需求的基础上，请返回后勤部需要准备的 最小 展台数量。
# 注意：
# 同一展台在不同天中可以重复使用。
# 示例 1：
# 输入：demand = ["acd", "bed", "accd"]
# 输出：6
# 解释： 第 0 天需要展台 a、c、d； 第 1 天需要展台 b、e、d； 第 2 天需要展台 a、c、c、d； 因此，后勤部准备 abccde 的展台，可以满足每天的展览需求;
# 示例 2：
# 输入：demand = ["abc", "ab", "ac", "b"]
# 输出：3
# 提示：
# 1 <= demand.length, demand[i].length <= 100
# demand[i][j] 仅为小写字母

class Solution(object):
    def minNumBooths(self, demand):
        """
        :type demand: List[str]
        :rtype: int
        """
        hash1 = [0] * 26
        len1 = len(demand)
        for i in range(len1):
            hash2 = [0] * 26
            len2 = len(demand[i])
            for j in range(len2):
                hash2[ord(demand[i][j]) - ord('a')] += 1
            for j in range(26):
                hash1[j] = max(hash1[j], hash2[j])
        return sum(hash1)

if __name__ == '__main__':
    s = Solution()
    demand = ["acd", "bed", "accd"]
    print(s.minNumBooths(demand))
    demand = ["abc", "ab", "ac", "b"]
    print(s.minNumBooths(demand))