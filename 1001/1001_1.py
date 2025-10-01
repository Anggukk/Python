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
