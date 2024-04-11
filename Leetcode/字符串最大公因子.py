# 1701.字符串最大公因子
# 对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
#
# 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_str = self.gcd_of_strings(str1, str2)
        if gcd_str and str1.count(gcd_str) * len(gcd_str) == len(str1) and str2.count(gcd_str) * len(gcd_str) == len(str2):
            return gcd_str
        else:
            return ""
    def gcd_of_strings(self,str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return str1[:gcd(len(str1), len(str2))]

if __name__ == '__main__':
    a = Solution()
    b = a.gcdOfStrings("ABCABC", "ABC")
    c = a.gcdOfStrings("ABABAB", "ABAB")
    d = a.gcdOfStrings("LEET", "CODE")
    print(f"b={b}, c={c}, d={d}")