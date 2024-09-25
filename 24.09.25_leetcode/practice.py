# 2024.09.25力扣网刷题
# 字母异位词分组——数组、哈希表、字符串、排序——中等
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出 : [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# 示例 2 :
# 输入 : strs = [""]
# 输出 : [[""]]
# 示例 3 :
# 输入 : strs = ["a"]
# 输出 : [["a"]]
# 提示：
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 方法一：哈希表
        hash_dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hash_dic:
                hash_dic[key].append(s)
            else:
                hash_dic[key] = [s]
        return list(hash_dic.values())


str =  ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(str))
