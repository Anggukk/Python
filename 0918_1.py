'''
# 이중 while 문

i = 2
while i < 10:
    j = 1
    print(f"=== {i}단 ===")
    while j < 10:
        print(f"{i} * {j} = {i*j}")
        j += 1
    print("")
    i += 1
'''


'''
# 실습3
# 문제1
real_id = "id"
real_password = "password"

id = input("ID 입력 : ")
password = "0"


while password != real_password:
    while id != real_id:
        print("ID가 존재하지 않습니다.")
        id = input("ID 입력 : ")
    password = input("비밀번호 입력 : ")
    if password != real_password:
        print("비밀번호가 틀렸습니다.")
print("로그인 성공!")
'''


# 함수
# 함수는 특정 작업을 수행하는 코드의 묶음입니다.
# 한 번 정의하면 필요할 때마다 호출하여 재사용할 수 있습니다.

# 함수를 사용하는 이유
# 1. 코드 재사용성 : 같은 코드를 반복 작성할 필요 없음
# 2. 모듈화 : 프로그램을 작은 단위로 나누어 관리
# 3. 가독성 향상 : 코드의 의도를 명확히 표현
# 4. 유지보수 용이 : 수정이 필요할 때 함수만 변경
# 5. 추상화 : 복잡한 로직을 단순한 인터페이스로 제공


# 함수 사용 - 코드 재사용
def print_section(title):
    print("="*20)
    print(f"{title} 섹션")
    print("="*20)


print_section("첫 번째")
print_section("두 번째")


# 함수 정의와 호출
# 함수 정의 (Defintion)
'''
def 함수이름(매개변수):
    실행 코드
    return 반환값
'''


# 함수 호출 (Call)
'''
결과 = 함수이름(인자)
'''


def say_hello():
    print("안녕하세요")


say_hello()


def greet(name):
    print(f"안녕하세요 {name}님!")


greet("김철수")
print(greet("이영희"))


def add(a, b):
    result = a+b
    return result


sum_result = add(3, 5)
print(sum_result)


# 사각형 넓이
def calculate_area(width, height):
    return width*height


print(calculate_area(10, 20))


'''
# 실습1
# 문제1
def calculate(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return float(a/b)
    else:
        return "지원하지 않는 연산입니다."


a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))
operator = input("연산자를 입력하세요 : ")

# result = calculate(a, b, operator)
# print(result)

print(calculate(a, b, operator))
'''


def greet(name, message="안녕!"):
    print(f"{name} {message}")


greet("은경")
greet("김철수", "안녕하세요")


'''
# 실습2
# 문제1
def average(*args):
    return sum(args)/len(args)


nums = list(map(int, input("숫자들을 입력하세요 : ").split()))
print(average(*nums))
'''


'''
# 문제2
def longest(*args):

    return max(args, key=len)


string = list(input("문자열들을 입력하세요 : ").split())
print(longest(*string))
'''


'''
# 문제3
def user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


info = input("사용자 정보를 입력하세요 (key:value 형태로) : ").split()

kwargs_dict = {}

for x in info:
    key, value = x.split(":")

    if value.isdigit():
        value = int(value)
    kwargs_dict[key] = value

user(**kwargs_dict)
'''


'''
# 문제4
def user(**kwargs):
    for key, value in kwargs.items():
        value = value*90/100
        print(f"{key} : {value}")


info = input("상품 가격 목록을 입력하세요(상품이름:가격 형태로) : ").split()

kwargs_dict = {}

for x in info:
    key, value = x.split(":")

    value = int(value)
    kwargs_dict[key] = value

user(**kwargs_dict)
'''


def calculate_stats(number):
    total = sum(number)
    avg = total/len(number)
    maxnum = max(number)
    minnum = min(number)

    return total, avg, maxnum, minnum


numbers = [100, 140, 230, 200]
a, b, c, d = calculate_stats(numbers)

print(a, b, c, d)


# return의 특징
def check_positive(number):
    if number > 0:
        return "양수"
    elif number < 0:
        return "음수"
    else:
        return "0"
    print("코드가 실행이 될까요?")


print(check_positive(4))


# 조기 반환(Early Return)
def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a/b


print(divide(10, 2))
print(divide(10, 0))


# 기본값 매개변수
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님")


greet("김철수")
greet("이영희", "반갑습니다")


# 여러 기본값
def create_profile(name, age=25, city="서울", job="개발자"):
    return {"name": name, "age": age, "city": city, "job": job}


print(create_profile("박민수"))
print(create_profile("김철수", 30, "부산"))


# 가변 위치 인자 (*args)
def sum_all(*numbers):
    print(type(numbers))
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))


# 가변 키워드 인자(**Kwargs)
def print_info(**user):
    print(type(user))
    print(user)
    for key, value in user.items():
        print(f"{key} : {value}")


print_info(name="김철수", age=20, city="서울")


def create_student(**info):
    student = {
        "name": info.get("name", "이름 없음"),
        "age": info.get("age", "20"),
        "grade": info.get("grade", 1),
        "subjects": info.get("subjects", []),
    }
    return student


student1 = create_student(name="김철수", subjects="python")
print(student1)
