# 실습3. 논리 연산과 조건 연산
# 1
import numpy as np

arr = np.array([5, 12, 18, 7, 30, 25])
print("문제1:", arr[(arr > 10) & (arr < 20)])


# 2
arr = np.array([10, 15, 20, 25, 30, 35])
print("문제2:", arr[(arr <= 15) | (arr >= 30)])


# 3
arr = np.array([3, 18, 15, 6, 2, 20])
arr[(arr >= 10)] = 0
print("문제3:", arr)


# 4
arr = np.array([7, 14, 21, 28, 35])
arr4 = np.where(arr >= 20, "High", "Low")
print("문제4:", arr4)


# 5
arr = np.arange(0, 10)
arr[arr % 2 != 0] *= 10
print("문제5:", arr)


# 6
arr = np.array([
    [10, 25, 30],
    [40, 5, 15],
    [20, 30, 50]
])
print("문제6:", arr[(arr >= 20) & (arr <= 40)])


# 7
arr = np.array([1, 2, 3, 4, 5, 6])
print("문제7:", arr[arr % 3 != 0])


# 8
arr = np.random.randint(0, 100, 10)
arr[arr < 50] = 50
print("문제8:", arr)


# 9
arr = np.array([
    [5, 50, 95],
    [20, 75, 10],
    [60, 30, 85]
])
arr9 = np.where(arr >= 70, "A", np.where((arr >= 30) & (arr < 70), "B", "C"))
print("문제9:\n", arr9)


# 차원 추가와 제거
# newaxis 와 expand_dims
# 새로운 차원을 추가하여 브로드 캐스팅이나 연산을 가능하게 한다
arr = np.array([1, 2, 3, 4, 5])
print("원본 : ", arr)
print("모양 : ", arr.shape)


# newaxis
row_vec = arr[np.newaxis, :]
print("행 벡터  : ", row_vec)
print("행 벡터 shape : ", row_vec.shape)

col_vec = arr[:, np.newaxis]
print("열 벡터 : \n", col_vec)
print("열 벡터 shape : ", col_vec.shape)


arr_expanded0 = np.expand_dims(arr, axis=0)
print("axis=0 \n", arr_expanded0)

arr_expanded1 = np.expand_dims(arr, axis=1)
print("axis=1 \n", arr_expanded1)


# squeeze
arr = np.array([
    [
        [1, 2, 3]
    ]
])
print("원본 : \n", arr)


squeezed = np.squeeze(arr)
print("squeezed \n", squeezed)
print("sqeezed 모양 \n", squeezed.shape)

squeezed0 = np.squeeze(arr, axis=0)
print("squeezed0 \n", squeezed0)
print("squeezed0 모양 \n", squeezed0.shape)


# 배열 평탄화 Flattening

# flatten : 항상 복사본 반환 (안전하지만 메모리 사용)
# ravel : 가능하면 뷰 반환 (빠르지만 주의 필요)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2차원 배열\n", arr)

flattened = arr.flatten()
print("flattened  결과 : ", flattened)

flattened[0] = 999      # 원본값은 변경 안됨
print(arr)
print(flattened)

raveled = arr.ravel()
print("raveled 결과 : ", raveled)

raveled[0] = 999        # 원본값도 변경 !!
print(arr)
print(raveled)


# 배열 결합 (Concatenation)

# 배열 이어 붙이기
# 같은 차원의 배열들을 특정 축을 따라 연결
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_1d = np.concatenate([a, b, c])
print("결합 결과", concat_1d)

# 2차원 배열 결합
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])

concat_v = np.concatenate([A, B], axis=0)
print("axis=0(수직결합):\n", concat_v)

concat_h = np.concatenate([A, B], axis=1)
print("axis=1(수평결합):\n", concat_h)


# vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack([a, b])
print("v stack (수직)\n", vstacked)

hstacked = np.hstack([a, b])
print("h stack (수평)\n", hstacked)


# 배열 분할
# split

# 하나의 배열을 여러 개의 작은 배열로 나누는 작업
# 데이터를 배치로 나누거나 훈련/검증 세트로 분리할 때 사용
arr = np.arange(12)
print(arr)

splits_equal = np.split(arr, 3)    # 3개로 균등 분할
print("splits_equal\n", splits_equal)
for i, sub in enumerate(splits_equal):
    print(i+1, sub)


splits_idx = np.split(arr, [3, 7])  # 해당 인덱스에서 분할
for i, sub in enumerate(splits_idx):
    print(i+1, sub)


arr = np.arange(24).reshape(4, 6)

row_splits = np.split(arr, 2, axis=0)
for i, sub in enumerate(row_splits):
    print(i+1, sub)


col_splits = np.split(arr, 2, axis=1)
for i, sub in enumerate(col_splits):
    print(i+1, sub)


# argsort

names = np.array(["김철수", "이영희", "박민수", "정수진", "최동욱"])
scores = np.array([85, 92, 78, 95, 88])

for name, score in zip(names, scores):
    print(f"{name} {score}")


# 점수 순으로 정렬
sorted_ids = np.argsort(scores)[::-1]

for i, idx in enumerate(sorted_ids, 1):
    print(f"{names[idx]}{scores[idx]}")


'''
# 실습1. 배열 형태 변형, 차원 확장/축소
# 1
arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
arr1_1 = arr.ravel()
arr1_2 = arr.flatten()

arr[0, 0] = 999

print(arr1_1)
print(arr1_2)


# 2
img = np.random.rand(32, 32)
arr2 = np.expand_dims(img, 0)
print("문제2:", arr2.shape)


# 3
img = np.random.randint(0, 255, (1, 28, 28, 1))
arr3 = np.squeeze(img, 0)
arr3 = np.squeeze(arr3, 2)
print("문제3:", arr3.shape)


# 4
arr = np.array([
    [3, 1, 2, 2],
    [1, 2, 3, 1],
    [2, 2, 1, 4]
])
arr4 = arr.flatten()
arr4 = np.unique(arr4)
arr4 = np.expand_dims(arr4, 0)
print("문제4:", arr4)


# 5
arr = np.array([[[1], [3], [2], [1], [3], [2], [3], [1], [2], [3]]])
arr5 = np.squeeze(arr)
print("문제5:", arr5)
print(arr5.shape)
arr5 = np.unique(arr5)
print(arr5)

# 6
arr = np.array([
    [
        [0, 1, 2, 3],
        [1, 2, 3, 4],
        [2, 3, 4, 5]
    ],
    [
        [3, 4, 5, 6],
        [4, 5, 6, 7],
        [5, 6, 7, 8]
    ]
])
arr6 = np.unique(arr)
arr6 = np.expand_dims(arr6, 1)
print("문제6:\n", arr6)
print(arr6.shape)
'''


'''
# 실습2. 배열의 결합과 분리
# 1
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
arr1 = np.concatenate([a, b], axis=0)
print("문제1:\n", arr1)


# 2
a = np.arange(12)
arr2 = np.split(a, 3)
print("문제2:")
for x in arr2:
    print(x)


# 3
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
arr3 = np.stack((a, b, c), axis=0)
print("문제3:\n", arr3)


# 4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
arr4 = np.stack((a, b), axis=1)
print("문제4:\n", arr4)
print(arr4.shape)


# 5
arr = np.arange(8)
arr5 = np.split(arr, [2, 5])
print("문제5:")
for x in arr5:
    print(x)


# 6
a = np.ones((2, 3))
b = np.zeros((2, 3))
arr6_1 = np.stack((a, b), axis=0)
arr6_2 = np.stack((a, b), axis=1)
print("문제6:")
print(arr6_1)
print(arr6_1.shape)
print("=================")
print(arr6_2)
print(arr6_2.shape)
'''


# 실습3. 배열의 정렬
# 1
arr = np.array([7, 2, 9, 4, 5])
arr1 = np.sort(arr)
print(f"""문제1:
오름차순 : {arr1}
내림차순 : {arr1[::-1]}""")


# 2
arr = np.array([
    [9, 2, 5],
    [3, 8, 1]
])
arr2 = np.sort(arr, 1)
print("문제2:\n", arr2)


# 3
arr = np.array([10, 3, 7, 1, 9])
arr3 = np.argsort(arr)
print(f"""문제3
인덱스 배열 : {arr3}
원본 배열 재정렬 : {arr[arr3]}""")


# 4
arr = np.array([
    [4, 7, 2],
    [9, 1, 5],
    [6, 8, 3]
])
arr4 = np.sort(arr, 0)
print("문제4:\n", arr4)
