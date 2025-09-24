# 모듈
'''
파이썬 코드가 저장된 파일
함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있습니다.

도구상자 : 여러 도구(함수)를 모아둔 상자(모듈)
'''


# 코드 재사용 : 한 번 작성한 코드를 여러 곳에서 사용
# 유지 보수 : 기능별로 분리하여 관리가 쉬움
# 협업 : 팀원들과 코드 공유가 편리
# 네임스페이스 : 이름 충돌 방지


# 전체 모듈 가져오기
import random
import math
import calculator


# 작성 되어 있는 모듈


result = calculator.add(10, 5)
print(result)


# 실습1


print(calculator.add(5, 6))
print(calculator.subtract(10, 3))
print(calculator.multiply(4, 5))
print(calculator.divide(5, 4))

print(calculator.divide(5, 0))


# 가상환경
# 프로젝트별로 독립적인 패키지 환경을 만들 수 있다.


# pip
# 파이썬 패키지 관리자


# 가상 환경 생성
# python -m venv 이름(myenv)


# 가상 환경 활성화
# myenv/Scripts/activate
# source myenv/Scripts/activate


# 가상 환경 비활성화
# deactivate


# 실습2
# 문제1


def dot(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))


p1 = list(map(int, input("x1 y1 : ").split()))
p2 = list(map(int, input("x2 y2 : ").split()))


print(round(dot(p1, p2), 2))


# 문제2
print(f"최대공약수 : {math.gcd(18, 24)}")
print(f"최소공배수 : {math.lcm(18, 24)}")


# 실습3

lotto = random.sample(range(1, 46), 6)
lotto.sort()
print(lotto)


# 실습4
user = input("가위/바위/보 : ")
computer = random.choice(["가위", "바위", "보"])
print("컴퓨터 : ", computer)

if user == "가위":
    if computer == "가위":
        print("무")
    elif computer == "바위":
        pinrt("패")
    else:
        print("승")
elif user == "바위":
    if computer == "가위":
        print("승")
    elif computer == "바위":
        pinrt("무")
    else:
        print("패")
else:
    if computer == "가위":
        print("패")
    elif computer == "바위":
        pinrt("승")
    else:
        print("무")
