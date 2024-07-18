# 2024.07.18力扣网刷题
# 最常见的单词——数组、哈希表、字符串、计数——简单
# 给你一个字符串 paragraph 和一个表示禁用词的字符串数组 banned ，返回出现频率最高的非禁用词。题目数据 保证 至少存在一个非禁用词，且答案 唯一 。
# paragraph 中的单词 不区分大小写 ，答案应以 小写 形式返回。
# 示例 1：
# 输入：paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# 输出："ball"
# 解释：
# "hit" 出现了 3 次，但它是禁用词。
# "ball" 出现了两次（没有其他单词出现这么多次），因此它是段落中出现频率最高的非禁用词。
# 请注意，段落中的单词不区分大小写，
# 标点符号会被忽略（即使它们紧挨着单词，如 "ball,"），
# 并且尽管 "hit" 出现的次数更多，但它不能作为答案，因为它是禁用词。
# 示例 2：
# 输入：paragraph = "a.", banned = []
# 输出："a"
# 提示：
# 1 <= paragraph.length <= 1000
# paragraph 由英文字母、空格 ' '、和以下符号组成："!?',;."
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] 仅由小写英文字母组成

# class Solution(object):
#     def mostCommonWord1(self, paragraph, banned):
#         """
#         :type paragraph: str
#         :type banned: List[str]
#         :rtype: str
#         """
#         mytable = paragraph.maketrans("!?',;.", '      ')
#         paragraph = paragraph.translate(mytable)
#         # 转小写并进行分割
#         word_list = paragraph.lower().split()
#         # 创建字典
#         word_dict = {}
#         max = 0
#         for word in word_list:
#             if word not in banned:
#                 if word not in word_dict:
#                     word_dict[word] = 1
#                 else:
#                     word_dict[word] += 1
#                 if word_dict[word] > max:
#                     max = word_dict[word]
#                     ans = word
#         return ans


def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    # 转小写并进行分割
    word_list = paragraph.lower().split()
    # 去标点符号
    for i in range(len(word_list)):
        if not word_list[i].isalpha():
            word_list[i] = list(word_list[i])
            for j in range(len(word_list[i])):
                if word_list[i][j] in "!?',;.":
                    word_list[i][j] = ' '
            word_list[i] = "".join(word_list[i])
    word_list = " ".join(word_list).split()
    # 创建字典
    word_dict = {}
    max = 0
    ans = word_list[0]
    for word in word_list:
        if word not in banned:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
            if word_dict[word] > max:
                max = word_dict[word]
                ans = word
    return ans


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# print(Solution().mostCommonWord(paragraph, banned))
print(mostCommonWord(paragraph, banned))