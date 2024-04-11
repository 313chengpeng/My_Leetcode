# 1768.交替合并字符串
# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
#
# 返回 合并后的字符串

class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        merged = ''
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        merged += word1[i:] + word2[j:]

        return merged


if __name__ == '__main__':
    a = Solution()
    b = a.mergeAlternately("abc", "pqr")
    c = a.mergeAlternately("ab", "pqrs")
    d = a.mergeAlternately("abcd", "pq")
    print(f"b={b}, c={c}, d={d}")
