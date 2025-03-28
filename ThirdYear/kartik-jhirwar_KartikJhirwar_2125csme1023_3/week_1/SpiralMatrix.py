class Solution:
    def spiralOrder(self, matrix):
        ans = []
        m, n = len(matrix), len(matrix[0])
        t, r, b, l = 0, n - 1, m - 1, 0
        while t <= b and l <= r:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r or t > b:
                break
            for i in range(r, l - 1, -1):
                ans.append(matrix[b][i])
            b -= 1
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans
