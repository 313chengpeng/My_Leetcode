# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[n][m]

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "a"))  # False
    print(s.isMatch("aa", "a*"))  # True
    print(s.isMatch("ab", ".*"))  # True
    print(s.isMatch("aab", "c*a*b"))  # True
    print(s.isMatch("mississippi", "mis*is*p*."))  # False
    print(s.isMatch("ab", ".*c"))  # False
    print(s.isMatch("aaa", "a*a"))  # True
    print(s.isMatch("aaa", "ab*a*c*a"))  # True
    print(s.isMatch("a", "ab*"))  # True
    print(s.isMatch("a", "ab*a"))  # False