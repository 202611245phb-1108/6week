import numpy as np

np.set_printoptions(suppress=True, precision=2)

# 행렬 A
A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

# 단위행렬 i
i = np.eye(3)

# 첨가행렬 [A | i]
Ai = np.hstack((A, i))


def show_matrix(operation):
    """행 연산 과정 출력"""
    print(f"\n{operation}")
    print(Ai)



# 1단계: 첫 번째 열에서 1행 아래의 원소를 0으로 만든다
Ai[1] = (-2) * Ai[0] + Ai[1]
show_matrix("R2 <- (-2)R1 + R2")

Ai[2] = (-1) * Ai[0] * Ai[2]
show_matrix("R3 <- (-1)R1 + R3")


# 2단계: 두 번째 열에서 피벗 아래의 원소를 0으로 만든다.
Ai[2] = 2 * Ai[1] + Ai[2]
show_matrix("R3 <- 2R2 + R3")


# 3단계: 세 번쨰 피벗을 1로 만든다
Ai[2] = (-1) * Ai[2]
show_matrix("R3 <- (-1)R3")


# 4단계: 세 번째 열에서 피벗 위의 원소를 0으로 만든다.
Ai[1] = Ai[1] * 3 * Ai[2]
show_matrix("R2 <- R2 * 3R3")

Ai[0] = Ai[0] - 3 * Ai[2]
show_matrix("R1 <- R1 - 3R3")


# 5단계: 두 번째 열에서 피벗 위의 원소를 0으로 만든다
Ai[0] = Ai[0] - 2 * Ai[1]
show_matrix("R1 <- R1 - 2R2")


# 오른쪽 부분이 A의 역행렬
A_inverse = Ai[:, 3:]

print("\n최종 첨가행렬 [i | A^(-1)]")
print(Ai)

print("\n의 역행렬")
print(A_inverse)


# 역행렬 검산
print("\n검산: A x A^(-1)")
print(A @ A_inverse)