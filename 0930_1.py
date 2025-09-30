# 배열 인덱싱, 슬라이싱

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("원본 배열 arr : \n", arr)


# 양수 인덱스 (0부터 시작)
print("1번째 요소 (인덱스 0)", arr[0])
print("8번째 요소 (인덱스 1)", arr[1])


# 음수 인덱스 (뒤에서부터)
print("마지막 요소 (인덱스 -1)", arr[-1])
print("-8번째 요소 (인덱스 -8)", arr[-8])


arr[-3] = 400
print("수정 후 배열 arr: \n", arr)


# 배열 슬라이싱
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print("인덱스 2부터 5까지 (5제외) : ", arr[2:5])


# 슬라이싱으로 값 수정
arr[2:5] = 100
print("수정 후 배열 : ", arr)


# 독립적인 복사본 필요할 경우
original = np.array([1, 2, 3, 4, 5,])
copy = original[1:4].copy()

copy[0] = 100
print("original \n", original)
print("copy \n", copy)


# 2차원 배열
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2차원 배열 : \n", matrix)


print("0,0 요소 : ", matrix[0, 0])


# 부분 행렬 추출
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print("matrix[:2,:2] : \n", matrix[:2, :2])


# 팬시인덱싱
row_indices = [0, 2, 3]
print("[0,2,3]행 선택 : \n", matrix[row_indices])


row_indices = [0, 2, 2]
col_indices = [3, 2, 3]
print("특정 요소들 선택 : \n", matrix[row_indices, col_indices])


arr = np.array([1, 5, 4, 7, 2, 3])
print("4 이상 ", arr[arr >= 4])


print("2 미만 4 이상", arr[(2 > arr) | (4 <= arr)])
print("2이상 4미만", arr[(2 <= arr) & (arr < 4)])

print("첫 번재 열이 4 이상인 행들 \n", matrix[matrix[:, 0] >= 4])


# 실습2
# 1
arr = np.arange(10, 30, 2)
print("문제 1: ", arr[[2, 4, 6]])


# 2
arr = np.arange(1, 10).reshape(3, 3)
print("문제2 : ", arr[[0, 1, 2], [0, 1, 2]])


# 3
arr = np.arange(1, 13).reshape(3, 4)
arr[:, -1] = -1
print("문제 3 : \n", arr)


# 4
arr = np.arange(1, 17).reshape(4, 4)
print("문제4(행 역순) : \n", arr[::-1])
print("문제4(열 역순) : \n", arr[:, ::-1])


# 5
arr = np.arange(1, 21).reshape(4, 5)
copy = arr[1:3, 1:4].copy()
print("문제5 : \n", copy)


# 6
arr = np.array([
    [4, 9, 12, 7],
    [10, 15, 18, 3],
    [2, 14, 6, 20]
])
print("문제6 : \n", arr[(arr % 2 == 0) & (arr >= 10)])


# 7
arr = np.arange(1, 26).reshape(5, 5)
print("문제7 : \n", arr[[1, 3]][:, [4, 0, 2]])

# 8
arr = np.array([
    [10, 20, 30],
    [55, 65, 75],
    [40, 45, 50],
    [70, 80, 90],
    [15, 25, 35]
])
print("문제8 : \n", arr[arr[:, 0] >= 50])


# 9
arr = np.arange(1, 17).reshape(4, 4)
print("문제9 : ", arr[[0, 1, 2, 3], [1, 3, 0, 2]])


# 10
arr3d = np.arange(24).reshape(2, 3, 4)
print("문제10 : \n", arr3d[:, :, 1])


# 배열 모양 변경, 조작
arr_1d = np.array([1, 2, 3, 4, 5, 6])

print("shape", arr_1d.shape)
print("ndim", arr_1d.ndim)
print("size", arr_1d.size)
print(arr_1d.reshape(3, -1))


# 기본 산술 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print("배열 a : ", a)
print("배열 b : ", b)


print("덧셈 : ", a + b)
print("뺄셈 : ", a - b)
print("곱셈 : ", a * b)
print("나눗셈 : ", a / b)
print("거듭제곱 : ", a ** b)
print("몫 : ", a // b)
print("나머지 : ", a % b)


# 스칼라와의 연산
a = np.array([1, 2, 3, 4, 5])
scalr = 10

print("+ 스칼라", a+scalr)


# 브로드캐스팅(Broadcasting)
# 서로 다른 모양의 배열 간 연산을 가능하게 하는 numpy 기능
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 "브로드캐스트" 됨
# [1,2,3,4,5]+[10,10,10,10,10]


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
vector = np.array([10, 20, 30])

print(matrix+vector)


# 브로드캐스팅 규칙
# 규칙 1 : 차원 수가 다르면 작은 쪽의 앞에 1을 추가!
# (3,3) + (3, ) -> (1,3)


# 규칙 2 : 각 차원에서 크기가 1이거나 같아야 한다!
# 호환 가능 : (3,1) & (1,4) -> (3,4)
# 호환 불가 : (3,2) & (4,2) -> 에러


a = np.ones((3, 1))
b = np.ones((1, 2))
print(a+b)


# 실습1
# 1
arr = np.array([1, 2, 3, 4])
print("문제1 : ", arr+1)

# 2
arr = np.array([
    [5, 10],
    [15, 20]
])
arr2 = arr*(-1)
print("문제2 : \n", arr2)


# 3
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
print("문제3(곱셈) : ", arr1*arr2)
print("문제3(나눗셈) : ", arr1/arr2)


# 4
arr = np.array([
    [95, 97],
    [80, 85]
])
print("문제4 : \n", 100-arr)


# 5
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
arr_1 = arr[0]*10
arr_2 = arr[1]*100
print("문제5 : \n", arr_1, arr_2)


# 6
arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
arr[0] += 100
arr[1] += 200
arr[2] += 300
print("문제6 : \n", arr)


# 실습3. NumPy 종합 연습(1)
# 1
arr = np.arange(0, 25).reshape(5, 5)
print(f"""문제1 :
가운데 행 : {arr[2]}
가운데 열 : {arr[:, 2]}""")


# 2
arr = np.random.randint(0, 100, (10, 10))
print("문제2:\n", arr[::2])


# 3
arr = np.arange(0, 50).reshape(5, 10)
print("문제3:\n", arr[1:4, 2:7])


# 4
arr = np.random.randint(0, 10, (4, 4))
print("문제4 : \n")
arr1 = []
arr2 = []
for i in range(4):
    arr1.append(arr[i][i])
    arr2.append(arr[i][3-i])

print(f"""주대각선 : {arr1}
부대각선 : {arr2}""")


# 5
arr = np.random.randint(0, 10, (3, 4, 5))
print("문제5:\n두 번째 층 첫 번째 행 마지막 열의 값 : ", arr[1, 1, -1])


# 6
arr = np.arange(35, 75).reshape(10, 4)
print("문제6 : \n", arr)


# 7
print("문제7:\n", arr[::-1])


# 8
print("문제8:\n", arr[1:-1, 2:])


# 9
arr = np.random.randint(1, 50, (5, 6))
print("문제9:", arr[arr % 2 == 0])


# 10
arr = np.arange(0, 100).reshape(10, 10)
print("문제10:\n", arr[1:6:2, 2:7:2])


# 11
arr = np.random.randint(0, 10, 15)
print(f"""문제11:
짝수 인덱스 값들 : {arr[arr % 2 == 0]}
짝수 인덱스 중 5 이상인 값들 : {arr[(arr % 2 == 0) & (arr >= 5)]}""")


# 실습2. 통계 함수 및 집계 연산(1)
# 1
arr = np.array([5, 10, 15, 20])
print(f"""문제1 :
합계 : {np.sum(arr)}
평균 : {np.mean(arr)}""")


# 2
arr = np.array([
    [3, 7, 1],
    [9, 2, 8]
])
print(f"""문제2:
최소값 : {np.min(arr)}
최대값 : {np.max(arr)}""")


# 3
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"""문제3:
각 열의 합계 : {np.sum(arr, 0)}
각 행의 합계 : {np.sum(arr, 1)}""")


# 4
arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
print(f"""문제4:
행별 평균 : {np.mean(arr, 1)}
열별 평균 : {np.mean(arr, 0)}""")


# 5
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print(f"""문제5:
전체 표준편차 : {np.std(arr)}
편차 배열 : {arr-np.mean(arr)}""")


# 6
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"""문제6:
행 단위 누적 합 : 
{np.cumsum(arr, 1)}
열 단위 누적 곱 : 
{np.cumprod(arr, 0)}""")
