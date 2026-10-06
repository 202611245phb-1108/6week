import numpy as np
np.set_printoptions(suppress=True, precision=2)

# 계수행렬 A
A = np.array([
    [1, -1, 1],
    [1, 1, -2],
    [1, 2, 1]
], dtype=float)

# 상수벡터 b
b = np.array([0, 1, 6], dtype=float)
# 기존 행렬식 D = det(A)
D = round(np.linalg.det(A))

print("계수행렬 A")
print(A)
print("\n상수벡터 b")
print(b)
print(f"\nD = det(A) = {D}")

if D == 0:
    print("det(A)가 0이므로 크래머의 규칙을 적용할 수 없습니다.")
else:
    determinants = []
    soultion = []
    # A의 각 열을 b로 교체
    for i in range(A.shape[1]):
        Ai = A.copy()
        Ai[:, i] = b

        Di = round(np.linalg.det(Ai))
        xi = Di / D
        determinants.append(Di)
        soultion.append(xi)

        print(f"\nA{i + 1}: {i + 1}번째 열을 b로 교체")
        print(Ai)
        print(f"D{i + 1} = D{i + 1}/D"
              f"= {Di}/{D} = {xi}"
        )
    soultion = np.array(soultion)

    print("\n최종 해")
    for i, value in enumerate(soultion, start=1):
        print(f"x{i} = {value}")
    # 검산
    print("\n검산 결과 A @ x")
    print(A @ soultion)
    print("\n원래 상수벡터 b")
    print(b)