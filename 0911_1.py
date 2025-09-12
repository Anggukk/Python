# 비교연산자
x = 10
y = 20

print(f"x == y : {x == y}")
print(f"x != y : {x != y}")
print(f"x < y : {x < y}")
print(f"x > y : {x > y}")
print(f"x <= y : {x <= y}")
print(f"x >= y : {x >= y}")


# 논리연산자
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(f"not True : {not True}")
print(f"not False : {not False}")


# 조건문
a = 10
if a != 10:
    print("if문 블럭 안")
print("if문 블럭 밖")


name = "Alice"  # 빈 문자열이 아니기 때문에 True 값으로 취급
if name:
    print("문자열이 존재합니다.")


name = ""  # False
if name:
    print("이름이 존재합니다.")


age = 20
if age >= 18:
    print("성인입니다.")


if True:  # 조건문을 넘기고싶으면 pass 입력 (들여쓰기는 필수로 있어야함)
    pass
print("조건문과 상관없습니다.")


'''
# 실습1
weather = input("날씨(비 or 맑음) : ")

if weather == "비":
    print("우산을 챙기세요!")
else:
    print("선크림을 바르세요!")
'''


name = ""

if name:
    print(f"이름은 : {name}")
else:
    print("이름을 작성해주세요")


'''
# 실습2
num = int(input("정수를 입력해주세요 : "))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
'''


age = 20
name = "철수"
grade = 2

if name:
    print(f"이름 : {name}")

if age > 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

if grade > 3:
    print("고학년입니다.")
elif grade == 2:
    print("2학년입니다.")
else:
    print("1학년입니다.")


'''
# 실습3
age = int(input("나이를 입력하세요 : "))

if age >= 19:
    print("청소년 관람불가 가능")
elif age >= 16:
    print("15세 이상 관람가")
elif age >= 13:
    print("12세 이상 관람가")
else:
    print("전체 관람가")
'''


'''
# 실습4
second = int(input("초를 입력하세요 : "))
time = second

hour = second//3600
second %= 3600
minute = second//60
second %= 60

if time >= 3600:
    print(f"{hour}시간 {minute}분 {second}초")
elif time >= 60:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")
'''


'''
# 중첩조건문
# 실습5

money = int(input("금액 입력 : "))
food = input("식품명 입력(김밥, 삼각김밥, 도시락) : ")

if food == "도시락":
    if money >= 4000:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
elif food == "김밥":
    if money >= 2500:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
else:
    if money >= 1500:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")
'''


# for문
'''
for i in range(5):
    print(i)
'''


'''
for i in range(1, 5): # i=1~4
    print(i)
'''


'''
for i in range(2, 8, 2): # 2~7까지 2개 간격으로
    print(i)
'''


'''
# 구구단 만들기
# 4단

for i in range(1, 10):
    print(f"4 * {i} = {4*i}")
'''


'''
# 구구단 만들기

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
    print("=================")
'''


# 리스트 순회
fruits = ["사과", "바나나", "오렌지", "포도"]

for fruit in fruits:
    print(fruit)


scores = [65, 27, 87, 86]
total = 0
count = 0

for score in scores:
    count += 1
    total += score
    print(f"점수 : {score}")

print(f"총점 : {total}")
print(f"평균 : {total/count}")


'''
word = "Python"
print("===========")

for char in word:
    print(char, end="")
'''


# 별 패턴 1 : 직각삼각형

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")


# 별 패턴 2 : 정사각형
print("===============")

for i in range(1, 6):

    print("*****")
