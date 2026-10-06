import numpy as np

# 원래 행렬
A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

# (i, j)번째 행과 열을 제거한 소행렬
def get_minor(matrix, row, col):
    return np.delete(
        np.delete(matrix, row, axis=0),
        col,
        axis=1
    )

# 여인수행렬 계산
def cofactor_matrix(matrix):
    n = matrix.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            C[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    
    return C

# 행렬식 계산
det_A = round(np.linalg.det(A))

if det_A == 0:
    print("행렬식이 0이므로 역행렬이 존재하지 않습니다.")
else:
    # 1. 여인수행렬
    C = cofactor_matrix(A)
    # 2. 수반행렬 = 여인수행렬의 전치행렬
    adj_A = C.T
    # 3. 역행렬
    inverse_A = (1 / det_A) * adj_A
    # 부동소수점 오차 정리
    C = np.round(C, 10)
    adj_A = np.round(adj_A, 10)
    inverse_A = np.round(inverse_A, 10)

    print("행렬 A")
    print(A)
    print("\n여인수행렬 C")
    print(C)
    print("\n수반행렬 adj(A)")
    print(adj_A)
    print("\n역행렬 A^(-1)")
    print(inverse_A)
    print("\n검산 A x A^(-1)")
    print(np.round(A @ inverse_A, 10))
