# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


if __name__ == '__main__':
    # 构造二叉树
    tree_list = [1, None, 2, 3]  # 注意这里使用 None 而不是 null
    root = build_tree_from_list(tree_list)

    # 计算最大深度
    solution = Solution()
    print(solution.maxDepth(root))  # 输出: 3