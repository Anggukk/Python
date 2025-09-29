# Numpy

# Numpy는 C언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리

# 메모리 효율성
# 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 어버헤드가 큼
# Numpy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장


# 벡터화 연산
# 반복문 없이 전체 배열에 대한 연사을 한번에 수행

import numpy as np
print("Numpy 버전: ", np.__version__)
print("Numpy 설치 경로: ", np.__file__)


# ndarray(N-dimensional array) Numpy의 핵심 자료구조
# 같은 타입의 요소들을 담는 다차원 컨테이너

arr = np.array([1, 2, 3, 4, 5])

print("1. 객체 타입 : ", type(arr))
print("2. 데이터 타입 : ", arr.dtype)
print("3. 배열 모양 : ", arr.shape)
print("4. 차원 수 : ", arr.ndim)
print("5. 전체 요소 수 : ", arr.size)


python_list = [1, 2.5, "3.", True]
numpy_array = np.array([1, 2, "3", True])   # 자동 변환
print("파이썬 리스트 : ", python_list)
print("Numpy 배열 : ", numpy_array)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("리스트 더하기 : ", list1+list2)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Numpy 배열 더하기 : ", arr1+arr2)


# 실수 배열
float_array = np.array([1.1, 2.2, 3.3, 4.4, 5])
print("실수 배열 : ", float_array)
print("데이터 타입 : ", float_array.dtype)


# 타입을 명시적으로 지정 배열
specified_array = np.array(["1", "3.2", True, 4, 5], dtype=np.float32)
print("명시적 배열 : ", specified_array)
print("데이터 타입 : ", specified_array.dtype)


# 문자열 배열
string_array = np.array(["apple", "bamama", "cherry"])
print("문자열 배열 : ", string_array)
print("데이터 타입 : ", string_array.dtype)  # <U10 (글자수)(유니코드 문자열, 최대 10자)


matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])


print("2차원 배열 : ", matrix)
print("모양 : ", matrix.shape)
print("차원 : ", matrix.ndim)
print("크기 : ", matrix.size)


rows = []
for i in range(3):
    row = [i*3+j for j in range(4)]
    rows.append(row)

matrix2 = np.array(rows)
print("동적 생성 행렬 : ", matrix2)


# 3차원 배열(2 x 3 x 4)
# 2개의 3 x 4 행렬로 구성
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
])

print("3차원 배열 모양 : ", tensor.shape)
print("차원 : ", tensor.ndim)


# numpy 내장 함수로 배열 생성
# 연속된 숫자 배열 arrange
# 0부터 9까지
arr1 = np.arange(10)
print(arr1)

arr2 = np.arange(1, 10, 0.5)
print(arr2)


# 균등 간격 배열 linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5)
print(arr1)

'''
step=(stop-start)/-1
'''


arr2 = np.linspace(0, 10, 5, endpoint=False)
print("끝값 제외 : ", arr2)

'''
step=(stop-start)/num
'''


# 로그 간격 배열 Logspace
# Logspace(start,end,num)


# zeros : 0으로 채운 배열
zeros_id = np.zeros(5)
print("1차원 zeros : ", zeros_id)


zeros_2d = np.zeros((3, 4), dtype=int)
print("2차원 zeros : ", zeros_2d)


matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
zeros_copy = np.zeros_like(matrix)
print(zeros_copy)


ones_1d = np.ones(5)
print("1차원 ones : ", ones_1d)


ones_2d = np.ones((3, 4))
print("2차원 ones : ", ones_2d)


ones_2d_bool = np.ones((3, 4), dtype=bool)
print("1차원 ones : ", ones_2d_bool)


# full - 특정 값으로 채운 배열
full_array = np.full((3, 4), 7)
print(full_array)


full_like = np.full_like(matrix, 999)
print(full_like)


# 3 x 3 항등행렬
identity = np.eye(4)
print("3 x 3 항등행렬\n", identity)


# 0과 1 사이의 균일 분포
random_uniform = np.random.rand(3, 4)
print("0부터 1 균일 분포 : \n", random_uniform)


# rounded = np.rounded()


# 특정 범위의 균일 분포 (예: 10~20)
low, high = 10, 20
random_range = low+(high-low)*np.random.rand(3, 3)
print(random_range)


uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print(uniform)


# 정규 분포 난수
# 표준 정규 분포 (편균 0, 표준편차 1)
random_normal1 = np.random.randn(3, 3)
print("표준 정규 분포\n", random_normal1)


# 평균 100, 표준편차 15인 정규 분포
mean, std = 100, 5
scores = mean+std*np.random.randn(1000)
print("표준 정규 분포\n", scores[:10])
print("실제 평균", scores.mean())
print("실제 표준편차", scores.std())


# 정수 난수
# 0~9 사이의 정수 난수
random_int = np.random.randint(0, 10, size=(3, 4))
print("0~9 정수 난수\n", random_int)


# 주사위 시뮬레이션(1~6)
dice = np.random.randint(1, 6, size=10)
print("주사위 10번 굴리기\n", dice)


# 시드 설정(재현 가능한 난수)
np.random.seed(42)
random1 = np.random.rand(5)
print("첫 번째 난수 : ", random1)


np.random.seed(42)
random2 = np.random.rand(5)
print("두 번째 난수 : ", random2)
print("같은가?", np.array_equal(random1, random2))

random3 = np.random.rand(5)
print("세 번째 난수 : ", random3)


# 실습1
# 1
zeros = np.zeros((3, 4), dtype=int)
arr1 = np.full_like(zeros, 5)
print("문제1:\n", arr1)


# 2
arr2 = np.arange(0, 21, 2)
print("문제2:\n", arr2)


# 3
arr3 = np.random.rand(2, 3)
print("문제3:\n", arr3)


# 4
arr4 = np.random.randn(6)*20+100
print("문제4:\n", arr4)

arr4 = np.random.normal(100, 20, 6)
print(arr4)


# 5
arr5 = np.arange(1, 21)
arr5 = arr5.reshape(4, 5)
print("문제5:\n", arr5)


# 6
arr6 = np.linspace(0, 1, 12)
arr6 = arr6.reshape(3, 4)
print("문제6:\n", arr6)


# 7
arr7 = np.random.randint(0, 100, (10, 10))
arr7 = arr7+np.eye(10)
print("문제7:\n", arr7)


# 8
arr8 = np.random.randint(0, 10, (2, 3, 4))
print("문제8:\n", arr8)
