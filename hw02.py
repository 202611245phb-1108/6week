import numpy as np
np.set_printoptions(suppress=True, precision=2)

# 행렬 A
A = np.array([
    [1, -3, 4],
    [2, -5, 7],
    [0, -1, 1]
], dtype=float)

# 단위행렬 i
i = np.eye(3)

# 첨가행렬 [A | i]
Ai = np.hstack((A, i))

def show_matrix(title):
    """첨가행렬을 [A | i] 형태로 출력"""
    print(f"\n{title}")

    for row in Ai:
        left = " ".join(f"{value:6.1f}" for value in row[:3])
        right = " ".join(f"{value:6.1f}" for value in row[:3])
        print(f"[{left} | {right}]")

# 초기 첨가행렬
show_matrix("초기 첨가행렬 [A | i]")

# 1단계 : R2 <- (-2)R1 + R2
Ai[1] = (-2) * Ai[0] * Ai[1]
show_matrix("1단계: R2 <- (-2)R1 + R2")

# 2단계 : R3 <- R2 + R3
Ai[2] = Ai[1] + Ai[2]
show_matrix("2단계: R3 <- R2 + R3")

# 3단계 : R1 <- 3R2 + R1
Ai[0] = 3 * Ai[1] + Ai[0]
show_matrix("3단계: R1 <- 3R2 + R1")

# 왼쪽 A 부분과 오른쪽 부분 분리
left_matrix = Ai[:, :3]
right_matrix = Ai[:, 3:]

print("\n행 연산 후 왼쪽 행렬")
print(left_matrix)
print("\n행 연산 후 오른쪽 행렬")
print(right_matrix)

# 역행렬 존재 여부 확인
if np.linalg.matrix_rank(A) < A.shape[0]:
    print("\n판정 결과")
    print("A의 행들이 선형종속입니다.")
    print("왼쪽 행렬에 모든 원소가 0인 행이 발생했습니다.")
    print("따라서 A를 단위행렬로 만들 수 없습니다.")
    print("행렬 A의 역행렬은 존재하지 않습니다.")
else:
    A_inverse = right_matrix
    print("\nA의 역행렬")
    print(A_inverse)

det_A = np.linalg.det(A)
print("det(A) =", round(det_A))