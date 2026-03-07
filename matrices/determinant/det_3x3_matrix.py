'''

2×2 Matrix:

| a  b |
| c  d |  = ad - bc

Copy

3×3 Matrix:

| a  b  c |
| d  e  f |  = a·|e f| - b·|d f| + c·|d e|
| g  h  i |      |h i|     |g i|     |g h|

4×4 Matrix:

| a  b  c  d |
| e  f  g  h |  = a·|f g h| - b·|e g h| + c·|e f h| - d·|e f g|
| i  j  k  l |      |j k l|     |i k l|     |i j l|     |i j k|
| m  n  o  p |      |n o p|     |m o p|     |m n p|     |m n o|

'''

def det_3(a):
    a, b, c = a[0]
    d, e, f = a[1]
    g, h, i = a[2]

    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

A = [
    [2, -1, 4],
    [0, 3, 5],
    [7, 2, -6]
]

print(det_3(A))

'''

'''

def det_4(a):
    a, b, c, d = a[0]
    e, f, g, h = a[1]
    i, j, k, l = a[2]
    m, n, o, p = a[3]

    return (a * (f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)) -
            b * (e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)) +
            c * (e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)) -
            d * (e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m)))

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(det_4(A))

''' recursive solution '''

def det(A):
    n = len(A)
    
    if n == 1:
        return A[0][0]
    
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    result = 0
    for col in range(n):
        # Create submatrix by removing row 0 and current column
        sub = [[A[i][j] for j in range(n) if j != col] for i in range(1, n)]
        # Add/subtract element * determinant of submatrix
        result += ((-1) ** col) * A[0][col] * det(sub)

    return result
    
    
