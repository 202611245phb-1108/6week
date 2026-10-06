# 2x2 행렬의 행렬식 계산 함수
def determinant_2x2(matrix):
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )

# 계수행렬 A
A = [
    [3, -2],
    [-5, 4]
]
# 상수벡터 b
b = [6, 8]

# A1: A의 첫 번째 열을 b로 교체
A1 = [
    [b[0], A[0][1]],
    [b[1], A[1][1]]
]
# A2: A의 두 번째 열을 b로 교체
A2 = [
    [A[0][0], b[0]],
    [A[1][0], b[1]]
]

# 각각의 행렬식 계싼
D = determinant_2x2(A)
D1 = determinant_2x2(A1)
D2 = determinant_2x2(A2)

print("계수행렬 A =", A)
print("A1 =", A1)
print("A2 =", A2)
print("\ndet(A) =", D)
print("det(A1) =", D1)
print("det(A2) =", D2)

# 크래머의 규칙 적용
if D == 0:
    print("\ndet(A)가 0이므로 크래머의 규칙을 적용할 수 없습니다.")
else:
    x1 = D1 / D
    x2 = D2 / D
    print("\n크러머의 규칙 계산")
    print(f"x1 = det(A1) / det(A) = {D1} / {D} = {x1}")
    print(f"x2 = det(A2) / det(A) = {D2} / {D} = {x2}")
    print("\n선형시스템의 해")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

    # 검산
    result1 = 3 * x1 - 2 * x2
    result2 = -5 * x1 + 4 * x2
    print("\n검산")
    print(f"3x1 - 2x2 = {result1}")
    print(F"-5x1 + 4x2 = {result2}")