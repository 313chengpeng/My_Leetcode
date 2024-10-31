# 字典初始化：
# d = defaultdict(list)：创建一个默认值为列表的字典 d。这意味着如果访问一个不存在的键，字典会自动创建一个空列表作为该键的值。
# 遍历字符串列表：
# for s in strs:：遍历输入的字符串列表 strs。
# 排序并分组：
# d[''.join(sorted(s))].append(s)：
# sorted(s)：将字符串 s 中的字符排序，返回一个字符列表。
# ''.join(sorted(s))：将排序后的字符列表转换为字符串。
# d[''.join(sorted(s))].append(s)：将排序后的字符串作为键，将原字符串 s 添加到对应的值列表中。这样，所有字母异位词都会被分到同一个键下。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())
