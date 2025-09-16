# 딕셔너리(dict)
# Key-Value 쌍으로 데이터를 저장하는 자료구조
# 해시 테이블 기반으로 매우 빠른 검색 속도
# Python의 가장 강력하고 유용한 자료구조 중 하나


# 딕셔너리를 사용하지 않는 경우 - 두 개의 리스트로 관리

import copy
student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾으려면?
target_id = "20230002"
if target_id in student_ids:
    index = student_ids.index(target_id)
    name = student_names[index]
    print(name)


# 딕셔너리를 사용하는 경우 - 직관적이고 빠름
students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}

print(students["20230002"])


# 특징
# Key-Value 쌍 : 각 값에 고유한 키로 접근
# 빠른 검색 : 0(1) 시간 복잡도
# 변경 가능 (Mutable) : 요소 추가, 수정, 삭제 가능
# Key는 유일 : 중복 키 불가(값은 중복 가능)
# 순서 보장 : Python3.7+ 부터 삽입 순서 유지


# Dictionary 생성
# 1. 빈 딕셔너리 생성
empty_dict1 = {}  # dict
empty_dict2 = dict()  # dict
empty_set = set()  # set
print(type(empty_dict1))
print(type(empty_dict2))


# 2. 값이 있는 딕셔너리 생성
person = {
    "name": "김철수",
    "age": 25,
    "city": "seoul"
}
print(person)


# 3. dict() 생성자 사용
person2 = dict(name="이영희", age=25, city="seoul")

print(person2)


# 4. 리스트 / 튜플로부터 생성
pairs = [("a", 1), ("b", 2)]
dict_from_pairs = dict(pairs)
pairs = [["a", 1], ["b", 2]]
dict_from_list = dict(pairs)


print(dict_from_pairs)
print(dict_from_list)


# 5. zip()를 이용한 생성
keys = ["name", "age", "city"]
values = ["박민수", 21, "대전"]

person3 = dict(zip(keys, values))
print(person3)


# 6. dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

print(squares)


# 7. fromkeys() 메서드
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)

print(default_dict)


# Key로 사용 가능한 타입
# Hashable 타입만 key로 사용 가능
valid_dict = {
    1: "정수",
    3.14: "실수",
    "string": "문자열",
    (1, 2): "튜플",
    True: "불리언",
    frozenset([1, 2]): "frozenset"
}


'''
# UnHashable 타입은 key로 사용 불가
invalid_dict = {
    [1, 2]: "리스트",
    {1, 2}: "set",
    {"a": 1}: "딕셔너리"
}
'''


# 접근과 수정
student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학",
    "gpa": 3.7
}


# 1. 대괄호 표기법 (KeyError 위험)
name = student["name"]
print(name)

# grade = student["grade"]
# print(grade)


# get() 메서드 (안전한 접근)
major = student.get("major")
print(major)
grade1 = student.get("grade")
print(grade1)


# 기본값 지정
grade2 = student.get("grade", "N/A")
print(grade2)


# keys(), values(), items()
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))


# 값 수정, 추가
student["age"] = 23
print(student)

student["grade"] = 3
print(student)


# update() 메서드로 여러 값 한번에 수정, 추가
student.update({
    "gpa": 4.0,
    "city": "seoul",
    "email": "dmsrud@gmail.com"
})
print(student)

info_dict = {"age": 22, "grade": 1, "phone": "010-1234-1234"}
student.update(info_dict)
print(student)


# 값 삭제
# del 키워드
del student["grade"]
print(student)


# pop() 메서드 - 값을 반환하면서 삭제
popped = student.pop("email")
print(popped)
print(student)


# popitem() - 마지막 항목 제거
last_item = student.popitem()
print(last_item)
print(student)


student.clear()
print(student)


# 실습1
# 문제1
user = {}
user = {
    "username": "skywalker",
    "email": "sky@example.com",
    "level": 5
}
email_value = user["email"]
user["level"] = 6
print(user)

print(user.get("phone", "미입력"))

user.update({"nickname": "sky"})
user.pop("email")

user.setdefault("signup_date", "2025-07-10")
print(user)


# 문제2
student = {}
student = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}

student["David"] = 80
student.update({"Alice": 88})
student.pop("Bob")

print(student)


# 중요 메서드들

scores = {
    "김철수": 85,
    "이영희": 95,
    "박민수": 78
}


# setdefault() - 키가 없으면 추가, 있으면 기존 값
scores.setdefault("정수진", 88)
scores.setdefault("김철수", 100)
print(scores)


# copy() - 얕은 복사
scores_copy = scores.copy()
scores_copy["최동훈"] = 95
scores_copy["김철수"] = 10
print(scores)
print(scores_copy)


# deepcopy() - 깊은 복사
nested_dict = {
    "team1": {"leader": "김철수", "members": ["이영희", "박민수"]},
    "team2": {"leader": "정수진", "members": ["최동훈", "강미나"]}
}

shallow = nested_dict.copy()
deep = copy.deepcopy(nested_dict)

nested_dict["team1"]["members"].append("신입")
print("shallw", shallow["team1"]["members"])
print("deep", deep["team1"]["members"])


# 순회
scores = {
    "김철수": 85,
    "이영희": 95,
    "박민수": 78
}

for name in scores:
    print(name, scores[name])


# 평균 값 계산
average = sum(scores.values())/len(scores)
print(average)


# 실습1
# 문제1
numbers = [3, 6, 1, 8, 4]

'''
numbers2 = []

for i in range(0, 5):
    numbers2.append(numbers[i]*2)
'''

numbers2 = [x*2 for x in numbers]

print(numbers2)


# 문제2
words = ["apple", "banana", "kiwi", "grape"]

'''
length_word = []

for i in range(0, 4):
    length_word.append(len(word[i]))
'''

length_word = [len(word) for word in words]

print(length_word)


# 문제3
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

'''
x_values = []
y_values = []

for i in range(0, 4):
    x, y = coordinates[i]
    x_values.append(x)
    y_values.append(y)
'''

x_values = [x for x, y in coordinates]
y_values = [y for x, y in coordinates]

print(x_values)
print(y_values)


# 실습2
# 문제1
num = int(input("정수를 입력하세요 : "))
sum = 0

for i in range(1, num+1):
    sum += i

print(sum)


# 문제2
num = int(input("정수를 입력하세요 : "))

for i in range(1, 10):
    print(f"{num} * {i} = {num*i}")


# 문제3
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        sum += i

print(sum)


# 문제4
num = int(input("숫자를 입력하세요 : "))

for i in range(1, num+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)
