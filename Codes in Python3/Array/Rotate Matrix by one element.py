def rotateMatrix(mat, n, m):
    depth = min(m, n)
    for i in range(depth // 2):
        top = i
        left = i
        bottom = n - 1 - i
        right = m - 1 - i

        temp = mat[top][left]

        for j in range(left + 1, right + 1):
            mat[top][j], temp = temp, mat[top][j]
        for j in range(top + 1, bottom + 1):
            mat[j][right], temp = temp, mat[j][right]
        for j in range(right - 1, left - 1, -1):
            mat[bottom][j], temp = temp, mat[bottom][j]
        for j in range(bottom - 1, top - 1, -1):
            mat[j][left], temp = temp, mat[j][left]
