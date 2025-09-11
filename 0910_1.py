# 변수 - 데이터를 담는 상자
'''
변수란
게임 -> 플레이어의 점수를 기억
쇼피올 -> 상품의 가격을 저장
SNS -> 사용자의 이름을 기억

데이터를 저장하는 공간=변수
'''

'''
상자(변수)에 물건(데이터)을 넣습니다.
이름표(변수명)로 상자를 구분합니다.
필요할 때 상자에서 물건을 꺼내 사용합니다.
'''

age = 20
name = "김철수"
height = 175.5

# 변수의 값은 바꿀 수 있다.
age = 30
print(age)


# 스네이크 케이스(snake_Case)
student_name = "김철수"
user_age = 25
total_score = 100

x = 10
y = 20
x, y = y, x
# x,y=20,10

print(x, y)

X, Y = 30, 'a'
print('X', X, sep=",")
print("Y", Y)


# 자료형
# 정수, 실수, 문자, 문자열

print('"파이썬"은 가장 널리 사용되는 프로그래밍 언어 입니다.')

true = True
false = False

print('true', type(true))
print('false', false)


a = "1"
b = '1'
print(a)
print(type(a))

a1 = int(a)
b1 = float(b)
print(a1, type(a1))
print(b1, type(b1))


c = 2
d = 2.1
# 문자열 포매팅 : f-string
print(f'c의 숫자는 {c}입니다.')


title = 'Inception'
director = 'Christopher Nolan'
year = 2010
genre = 'Sci-Fi'

print(f'Title : {title} Director : {director} Year : {year} Genre : {genre}')


name = '정은경'
age = 25
mbti = 'ENFP'

# print(f"안녕하세요.\n제 이름은 {name}이고,\n{age}살입니다.\n제 MBTI는 {mbti}입니다.")
print(f"""안녕하세요.
제 이름은 {name}이고,
{age}살입니다.
제 MBTI는 {mbti}입니다.""")


# 연산자
a = 10
a += 5
print(a)  # 15

a -= 4
print(a)  # 11

a *= 3
print(a)  # 33

a /= 11
print(a)  # 3

'''
a //= 2
print(a)
'''

a %= 2
print(a)

a = 10
a %= 3
print(a)


# 실습1
money = 300000

money -= 80000
money -= 9000*5
money += 120000
money += money*0.2
money -= money/3

print(money)


'''
# 입력 : input() 함수
name = input("이름을입력하세요 : ")
score = int(input("점수를 입력하세요 : "))  # 연산을 하려면 int형으로 되어있어야함
print(name)
print(f'점수는 : {score+10}')
'''


'''
# split() 공백을 구분자로 나누겠다.
fruit = "사과 참외 수박".split()
print(fruit)


fruit1, fruit2, fruit3 = input("과익 3개 입력 : ").split()
print(fruit1, fruit2, fruit3)
'''


# 실습2
intro = "둠칫"
drop = "두둠칫"

print(intro+drop*3)


'''
# 실습3
name = input("이름 : ")
age = input("나이 : ")

print(f"안녕하세요. 저는 {name}이고, {age}살입니다.")
'''


# 실습4
width = int(input("가로 : "))
length = int(input("세로 : "))

print(f"""넓이: {width*length}
둘레: {width*2+length*2}""")


'''
num1, num2, num3, num4 = input("네 자릿수 정수: ").split()
print(f"""천의 자리 : {num1}
백의 자리 : {num2}
십의 자리 : {num3}
일의 자리 : {num4}
""")
'''

num = int(input("네 자릿수 정수 : "))

print(f"천의 자리 : {num//1000}")
num %= 1000
print(f"백의 자리 : {num//100}")
num %= 100
print(f"십의 자리 : {num//10}")
num %= 10
print(f"일의 자리 : {num}")


# 실습5
name1, name2, name3 = input("발표자 이름 3명을 입력하세요 : ").split()
subject1, subject2, subject3 = input("발표 주제 3개를 입력하세요 : ").split()

print(f"""발표 순서 안내입니다.

1조 발표자 : {name1} - 주제 : {subject1}
2조 발표자 : {name2} - 주제 : {subject2}
3조 발표자 : {name3} - 주제 : {subject3}""")


# 실습6
year, month, day = input("년, 월, 일을 입력해주세요(.로 구분) : ").split(".")
hour, minute, second = input("시, 분, 초를 입력해주세요(:로 구분) : ").split(":")

print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
시작 시간은 {hour}시 {minute}분 {second}초입니다.""")
