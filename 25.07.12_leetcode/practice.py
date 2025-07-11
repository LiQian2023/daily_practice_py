# 2025.07.12力扣网刷题
# IP 地址无效化——字符串——简单
# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
# 示例 1：
# 输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"
# 示例 2：
# 输入：address = "255.100.50.0"
# 输出："255[.]100[.]50[.]0"
# 提示：
# 给出的 address 是一个有效的 IPv4 地址


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


if __name__ == '__main__':
    s = Solution()
    print(s.defangIPaddr("1.1.1.1"))
    print(s.defangIPaddr("255.100.50.0"))