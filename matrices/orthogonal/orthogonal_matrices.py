import math
import random

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def norm(v):
    return math.sqrt(sum(x * x for x in v))

def scale(v, s):
    return [x * s for x in v]

def subtract(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def add(M1, M2):
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

def is_orthogonal(Q, tol=1e-10):
    """Check if matrix Q is orthogonal: Q^T * Q = I"""
    QTQ = multiply(transpose(Q), Q)
    I = identity(len(Q))
    return all(abs(QTQ[i][j] - I[i][j]) < tol for i in range(len(Q)) for j in range(len(Q[0])))

def gram_schmidt(A):
    """Generate orthogonal matrix using Gram-Schmidt orthogonalization"""
    n, m = len(A), len(A[0])
    Q = [[0.0] * m for _ in range(n)]
    for i in range(m):
        q = [A[j][i] for j in range(n)]
        for j in range(i):
            q_j = [Q[k][j] for k in range(n)]
            a_i = [A[k][i] for k in range(n)]
            q = subtract(q, scale(q_j, dot(q_j, a_i)))
        q_norm = norm(q)
        for k in range(n):
            Q[k][i] = q[k] / q_norm
    return Q

def qr_decomposition(A):
    """QR decomposition: A = Q * R where Q is orthogonal and R is upper triangular"""
    n, m = len(A), len(A[0])
    Q = [[0.0] * m for _ in range(n)]
    R = [[0.0] * m for _ in range(m)]
    
    for i in range(m):
        q = [A[j][i] for j in range(n)]
        for j in range(i):
            q_j = [Q[k][j] for k in range(n)]
            a_i = [A[k][i] for k in range(n)]
            R[j][i] = dot(q_j, a_i)
            q = subtract(q, scale(q_j, R[j][i]))
        R[i][i] = norm(q)
        for k in range(n):
            Q[k][i] = q[k] / R[i][i]
    
    return Q, R

def rotation_matrix_2d(theta):
    """Generate 2D rotation matrix"""
    return [[math.cos(theta), -math.sin(theta)],
            [math.sin(theta), math.cos(theta)]]

def rotation_matrix_3d(axis, theta):
    """Generate 3D rotation matrix using Rodrigues' formula"""
    n = norm(axis)
    axis = [x / n for x in axis]
    K = [[0, -axis[2], axis[1]],
         [axis[2], 0, -axis[0]],
         [-axis[1], axis[0], 0]]
    I = identity(3)
    K2 = multiply(K, K)
    return add(add(I, scale_matrix(K, math.sin(theta))), scale_matrix(K2, 1 - math.cos(theta)))

def scale_matrix(M, s):
    return [[M[i][j] * s for j in range(len(M[0]))] for i in range(len(M))]

if __name__ == "__main__":
    Q1 = [[1, 0], [0, 1]]
    print(f"Identity is orthogonal: {is_orthogonal(Q1)}")
    
    A = [[random.random() for _ in range(3)] for _ in range(3)]
    Q2 = gram_schmidt(A)
    print(f"\nGram-Schmidt result is orthogonal: {is_orthogonal(Q2)}")
    
    Q3 = rotation_matrix_2d(math.pi/4)
    print(f"\n2D rotation is orthogonal: {is_orthogonal(Q3)}")
    
    Q4 = rotation_matrix_3d([0, 0, 1], math.pi/3)
    print(f"3D rotation is orthogonal: {is_orthogonal(Q4)}")
    
    A2 = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]
    Q, R = qr_decomposition(A2)
    print(f"\nQR decomposition Q is orthogonal: {is_orthogonal(Q)}")
    QR = multiply(Q, R)
    print(f"Q*R reconstructs A: {all(abs(QR[i][j] - A2[i][j]) < 1e-10 for i in range(3) for j in range(3))}")
