# 2024.09.07力扣网刷题
# 寻找文件副本——数组、哈希表、排序——简单
# 设备中存有 n 个文件，文件 id 记于数组 documents。
# 若文件 id 相同，则定义为该文件存在副本。请返回任一存在副本的文件 id。
# 示例 1：
# 输入：documents = [2, 5, 3, 0, 5, 0]
# 输出：0 或 5
# 提示：
# 0 ≤ documents[i] ≤ n - 1
# 2 <= n <= 100000

class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        # 方法一：哈希表
        nums_dict = {}
        for i in documents:
            if i in nums_dict:
                return i
            nums_dict[i] = 1
        return -1