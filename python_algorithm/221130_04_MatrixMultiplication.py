# 행렬의 곱, 정방행렬 
# n * n의 행렬의 곱을 구하시오

def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    print(C)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print('A =', A)
print('B =', B)
C = matrixmult(A, B)
print('C =', C)

n = 2
D = [[0] * n for _ in range(n)]
print(D)

# >>> print(D)
# [[0, 0], [0, 0]] #결과값

