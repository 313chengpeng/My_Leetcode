# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

from typing import List
import time
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def backtrack(combination, nextdigit):
#             if len(nextdigit) == 0: res.append(combination)
#             else:
#                 for letter in phone[nextdigit[0]]:
#                     backtrack(combination + letter, nextdigit[1:])
#         if not digits: return []
#         phone = {
#                     "2":["a","b","c"],
#                     '3':['d','e','f'],
#                     '4':['g','h','i'],
#                     '5':['j','k','l'],
#                     '6':['m','n','o'],
#                     '7':['p','q','r','s'],
#                     '8':['t','u','v'],
#                     '9':['w','x','y','z']
#                 }
#         res = []
#         backtrack('',digits)
#         return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit)-ord('2')]:# 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

if __name__ == '__name__':
    solution = Solution()
    digits = '23'
    time.sleep(1)
    # quene = solution.letterCombinations(digits)
    print(solution.letterCombinations(digits))
