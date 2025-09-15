# Tuple
# 순서가 있는 불변 시퀸스 자료 구조
# 한 번 생성되면 수정할 수 없는 리스트와 유사한 구조
# 여러 개의 값을 하나의 다누이로 묶을 대 사용

# 왜 Tuple이 필요한가
# 변경되면 안되는 데이터 보호
# 리스 사용 시 -> 실수로 변경 가능


'''
coordinates_list = [37.345, 126.432]
coordinates_list[0] = 0

coordinates_list = (37.345, 126.432)
coordinates_list[0] = 0 #TypeError 발생 변경 불가능
'''


# 특징
# 불변성 : 생성 후 수정 불가능
# 순서 보장 : 인덱스로 접근 가능
# 해시 가능 : 딕셔너리 키로 사용 가능
# 메모리 효율적 : 리스트보다 적은 메모리 사용


# 1. 소괄호 사용
emp_tuple = ()
numbers = (1, 2, 3, 4, 5,)
mixed = (1, "hello", 3.14, True)
print("type(mixed) : ", type(mixed))
print("mixed : ", mixed)


# 2. 소괄호 없이 생성
numbers2 = 1, 2, 3, 4, 5
print("type(numbers2) : ", type(numbers2))


# 3. tuple() 생성자 사용
from_list = tuple([1, 2, 3, 4])
print("type(from_list) : ", type(from_list))

from_str = tuple("hello")
print("type(from_str) : ", type(from_str))


# 4. 단일 요소 튜플
single = (1,)
print("type(single) : ", type(single))


# 5. range로 튜플 생성
range_tuple = tuple(range(1, 10))
print("type(range_tuple) : ", type(range_tuple))
print("range_tuple : ", range_tuple)


# tuple 접근과 슬라이싱
fruits = ("사과", "바나나", "수박", "오렌지", "포도")

print(fruits[1])
print(fruits[-1])

print(fruits[1:3])
print(fruits[:2])
print(fruits[::-1])


# 슬라이싱으로 새 튜플 생성
first_three = fruits[:3]
print(first_three)
last_two = fruits[-2:]
print(last_two)


# 불변성 확인
numbers = (1, 2, 3, 4, 5, 6)


'''
# 수정 시도=모두 에러 발생
numbers[0] = 10
numbers.append(6)
del numbers[1]
'''

# 새 튜플 생성은 가능
new_numbers = numbers+(1, 2)
print(new_numbers)

tuple_with_list = ([1, 2], [3, 4])
tuple_with_list[0].append(3)
print(tuple_with_list)


# 언패킹(Unpacking)
coordinates = (3, 5)
x, y = coordinates
print(f"x = {x}, y = {y}")
x = 20
print(f"x = {x}, y = {y}")


'''
x, y = (10, 20, 30)  # ValueError
'''


numbers = (1, 2, 3, 4, 5,)
first, *middle, last = numbers
print(f"first : {first}\nmiddle : {middle}\nlast : {last}")


# 빈 리스트 생성
first, *rest = (1,)
print("first", first)
print("rest", rest)


# tuple 매서드
numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)

count_2 = numbers.count(2)
print(count_2)

index_4 = numbers.index(4)  # index() : 없는 값 검색 시 에러
print(index_4)


# value 값이 튜플에 있는지 확인하고 사용
value = 10
if value in numbers:
    print(f"{value}의 인덱스 : {numbers.index(value)}")
else:
    print(f"{value}는 튜플에 없습니다.")


# 연산
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1+tuple2)


# 곱셉(반복
print(tuple1*3)


tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print(tuple1 < tuple2)  # 앞에서부터 비교 (Ture 값이 앞에 나오면 Ture 출력)
print(tuple1 == tuple2)


# 길이, 최대, 최소, 합
numbers = (1, 2, 3, 4)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# 실습1
# Step1
user = ("minji", 25, "Seoul")

'''
user_list = list(user)
print(user_list)

user_list[0] = "eunji"

restored_user = user_list
print(restored_user)
'''


restored_user = ("eunji", user[1], user[2])
print(restored_user)

# Step2

name, age, city = restored_user


# Step3

if city == "Seoul":
    print("※서울 지역 보안 정책 적용 대상입니다.")
else:
    print("※일반 지역 보안 정책 적용 대상입니다.")


# Step4

users = ("minji", "eunji", "soojin", "minji", "minji")

print(users.count("minji"))
print(users.index("soojin"))


# Step5

sorted_users = list(users)
sorted_users.sort()

print(sorted_users)
