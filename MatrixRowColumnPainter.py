class Solution:
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])

        position_map = {}
        for i in range(m):
            for j in range(n):
                position_map[mat[i][j]] = (i, j)

        row_paint_count = [0] * m
        col_paint_count = [0] * n

        for idx, num in enumerate(arr):
            row, col = position_map[num]
            
            row_paint_count[row] += 1
            col_paint_count[col] += 1
            
            if row_paint_count[row] == n or col_paint_count[col] == m:
                return idx

        return -1  
sol = Solution()
print(sol.firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]))  # Output: 2
print(sol.firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]))  # Output: 3
