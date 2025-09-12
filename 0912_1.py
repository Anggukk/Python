# 컬렉션 자료형

list1 = list()
list2 = list("Hello")

print(list1)
print(list2)


# 인덱싱
print(list2[0])


# H  e  l  l  o
# 0  1  2  3  4
# -5 -4 -3 -2 -1


# 슬라이싱
# list3=list("Python")
text3 = "Hello"
print("text3[:]", text3[:])
print("text3[:3]", text3[:3])
print("text3[2:4]", text3[2:4])
print("text3[-3:-1]", text3[-3:-1])
print("text3[::-1]", text3[::-1])
print("text3[::-2]", text3[::-2])
print(text3[4:1:-1])


numbers = [10, 20, 30, 40]
print(numbers[1:3])

numbers[1:3] = [40, 20]
print(numbers)

numbers[1:3] = [40, 30, 20]
print(numbers)


# 실습1
# 문제1,2,3
nums = [10, 20, 30, 40, 50]
print(nums[::])

nums = [100, 200, 300, 400, 500, 600, 700]
nums2 = nums[2:5]
print(nums2)

nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2
print(nums)


# 문제4,5,6
items = ["a", "b", "c", "d", "e"]
print(items[::-1])

data = ["zero", "one", "two", "three", "four", "five"]
print(data[::2])

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print(movies)


# 문제7,8
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
subjects2 = subjects[3::2]
print(subjects2)

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data1 = data[:3]
data2 = data[3:6]
data3 = data[6:]
print(data1[::-1], data2[::-1], data3[::-1])
