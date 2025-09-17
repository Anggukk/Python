# while문
import random
i = 1

while i <= 5:
    print("반복문 실행")
    i += 1

print("반복문 종료")


'''
# 실습1
# 문제1
secret_code = "codingonre3"

code = input("비밀 코드를 입력하세요 : ")

while code != secret_code:
    code = input("비밀 코드를 입력하세요 : ")

print("입장이 허용되었습니다!")
'''


'''
# 문제2

random_value = random.randrange(1, 101)

n = 1
num = int(input("숫자 입력 : "))

while num != random_value:
    if num < random_value:
        print(f"{num}보다는 커요.")
    else:
        print(f"{num}보다는 작아요.")
    num = int(input("숫자 입력 : "))
    n += 1
print(f"{n}번 만에 정답을 맞췄습니다.")
'''


# for 문 vs while 문
# for 문 : 몇 번 반복할지 정해져 있을때
# while 문 : 조건이 만족하는 동안 계속 반복

# while 조건식 :
#   반복할 코드
#   (조건을 변경하는 코드)

# 카운트 다운
count = 5

while count > 0:
    print(count)
    count -= 1  # 중요! 조건을 변경

print("while 문 종료")


# 누적 합계 구하기
total = 0
num = 1

while num <= 100:
    total += num
    num += 1

print(f"1부터 100까지의 합 {total}")


# while 문으로 입력 검증하기
# 올바른 입력을 받을 때까지 반복
age = -1

while age < 0 or age > 150:
    age = int(input("나이를 입력하세요(0~150) : "))

    if age < 0 or age > 150:
        print("올바른 나이를 입력해주세요!")

print(f"입력된 나이 : {age}세")
