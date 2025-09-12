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


# 인덱스 요소 삭제
list = [10, 20, 30, 40, 50]

del list[3]
print(list)

del list[1:3]
print(list)


# 실습2
# 문제1
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]

del fruits[1:4]
print(fruits)


# 문제2
letters = ["A", "B"]
letters *= 3
del letters[2]
print(letters)


# 요소 추가 메서드
numbers = [10, 21, 15, 22, 54]

numbers.append(20)
print(numbers)

numbers.extend([5, 29])
print(numbers)

numbers.insert(2, 30)
print(numbers)


fruits = ["사과", "바나나", "오렌지", "바나나", "포도"]
fruits.remove("바나나")
print(fruits)

removed = fruits.pop()  # pop에 숫자 안쓰면 맨 뒤에꺼가 사라짐
print(removed)
print(fruits)

fruits.clear()  # 리스트는 삭제안되고 요소만 삭제됨
print(fruits)


# 요소 검색
numbers = [1, 2, 6, 9, 5, 3, 2, 4, 7]

idx = numbers.index(6)  # 6이 있는 자리 찾기
print(idx)

count = numbers.count(2)
print("count : ", count)

numbers.sort()
print(numbers)


# 리스트 정렬
numbers = [3, 1, 2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)


# 실습3
# 문제1
train = ["철수", "영희"]
train.extend(["민수", "지훈"])
train.remove("영희")
train.insert(1, "수진")
train.remove("민수")
train.reverse()
print(train)


# 문제2
list = [5, 3, 7]
list.extend([4, 9])
print(max(list))
print(min(list))
print(sum(list))
list.sort()
list.pop()
print(list)
