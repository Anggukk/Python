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
