import numpy as np
# 3차원 벡터
u1 = np.array([1, 1, 0], dtype=float)
u2 = np.array([1, 1, 1], dtype=float)
u3 = np.array([0, 2, 3], dtype=float)

# 각 벡터를 행으로 가지는 행렬
A = np.array([
    u1,
    u2,
    u3
])

print("벡터 행렬 A")
print(A)

# 행렬식 계싼
det_A = np.linalg.det(A)
# 부동소수점 오차 정리
det_A = round(det_A, 10)
# 평형육면체의 체적
volume = abs(det_A)

print("\n행렬식 det(A)")
print(det_A)
print("\n평형육면체 S의 체적")
print(volume)