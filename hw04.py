import numpy as np
np.set_printoptions(suppress=True, precision=2)

# 계수행렬 A
A = np.array([
    [1, 2, 3],
    [1, 3, 6],
    [2, 6, 13]
], dtype=float)

# 상수벡터 b
b = np.array([
    [1],
    [3],
    [5]
], dtype=float)

print("계수행렬 A")
print(A)
print("\n상수벡터 b")
print(b)

# 행렬식 계산
det_A = np.linalg.det(a)
print("\n행렬식 det(A)")
print(round(det_A, 10))

# 역행렬 존재 여부 확인
if np.isclose(det_A, 0):
    print("\ndet(A) = 0이므로 역행렬이 존재하지 않습니다.")
else:
    # A의 역행렬
    A_inverse = np.linalg.inv(A)

    print("\nA의 역행렬")
    print(A_inverse)
    # X = A^(-1)b
    X = A_inverse @ b
    print("\n선형시스템의 해")
    print(X)

    x, y, z = X.flatten()
    print(f"\nx = {x:.0f}")
    print(f"y = {y:.0f}")
    print(f"z = {z:.0f}")

    # 검산
    print("\n검산 결과 A @ X")
    print(A @ X)