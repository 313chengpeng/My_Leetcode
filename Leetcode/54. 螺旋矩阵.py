# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
from  typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        u,d,l,r = 0,len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while True:
            for i in range(l, r+1):
                res.append(matrix[u][i])
            u +=1
            if u > d:
                break
            for i in range(u, d+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l-1, -1):
                res.append(matrix[d][i])
            d -= 1
            if u > d:
                break
            for i in range(d, u-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]