# 现有一个狭小的老鼠洞，每次仅能一只老鼠进或者出（类似于栈的特性），如果通道里有多只老鼠，那么先进洞的老鼠会比晚进洞的老鼠出来更晚，假如有一窝老鼠来串门，我们给每只老鼠单独编个数字号码，1、2、3...
#
# 允许老鼠进洞后，又出洞，再次进洞，且若众多老鼠都挤满到洞口了，则不再会有老鼠进洞，最后出洞的顺序就按洞口到洞底的老鼠编号输出。
#
# 假如老鼠进洞的顺序是1、2、3，那么可能的出洞顺序是3、2、1， 考虑到洞未满的情况下，老鼠进洞后又出洞了，也可能是1、2、3等，但不可能是3、1、2。
#
# 现给定一个进洞序列，序列里数字可能重复，重复表示出洞后再次进洞，假定序列最后洞是满的，序列长度小于10000。 即老鼠编号范围是[1,10000]
#
# 请给出老鼠出洞的顺序？


def mouse_out_sequence(in_sequence):
    stack = []
    out_sequence = []

    for mouse in in_sequence:
        if not stack or stack[-1] != mouse:  # 如果栈为空或栈顶不是当前老鼠，则进洞
            stack.append(mouse)
        else:  # 栈顶是当前老鼠，意味着它要出洞
            out_sequence.append(stack.pop())

    # 将栈中剩余的老鼠出洞
    while stack:
        out_sequence.append(stack.pop())

    return out_sequence

# 示例
in_sequence = [1, 2, 3, 2, 1, 3]
print(mouse_out_sequence(in_sequence))