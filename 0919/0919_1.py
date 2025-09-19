# 지역 변수 - 함수 내부에서 선언 & 함수 내부에서만 사용 가능
# 전역 변수 - 함수 외부에서 선언 & 함수 내부에서도 사용 가능


# 중첩 함수

def outer():
    a = 10

    def inner():
        nonlocal a
        a += 5
        print(f"[inner] a: {a}")
    inner()
    print(f"[outer] a : {a}")


outer()


# 함수의 범위 (Scope)
'''
변수의 범위란?
변수가 살아있는(접근 가능한) 영역을 범위(Scope)라고 한다.
비유:
집 = 전역범위
방 = 지역범위
방 안의 물건은 그 방에서만 사용 가능
거실의 물건은 모든방에서 사용 가능
'''


# 전역 변수(Global Variable)
global_var = "전역 변수"


def my_fun():
    # 지역 변수(Local Varicalbe)
    local_var = "지역 변수"

    print(global_var)  # 전역 변수 접근 가능
    print(local_var)  # 지역 변수 접근 가능


my_fun()
print(global_var)  # 전역 변수 접근 가능
# print(local_var)  # 지역 변수 접근 불가능


# Global 키워드
# 함수 안에서 전역 변수를 수정하기 위해 global 키워드를 사용

count = 0  # 전역 변수


'''
def increment_wrong():
    count=count+1  # 에러 발생
'''


def increment_right():
    global count
    count = count+1


increment_right()
print(count)


score = 0


def add_score(points):
    global score
    score += points
    print(f"점수 획득! 현재 점수 : {score}")


def reset_score():
    global score
    score = 0
    print("점수 초기화!!")


add_score(100)
add_score(200)
print(score)

reset_score()
print(score)


# 전역 변수 사용 주의
# 전역 변수는 편리하지만 과도하게 사용하면 코드가 복잡해진다.

total = 0
count = 0


def add_number(num):
    global total, count
    total += num
    count += 1


def get_average():
    global total, count
    return total/count if count > 0 else 0


# 좋은 예
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)


numbers = [53, 56, 34, 64,]
avg = calculate_average(numbers)


# ==============================


def num_append(numbers):   # 리스트는 전역변수 global 사용 안해도 됨
    numbers.append(6)


numbers = [1, 2, 3, 4, 5]
print(numbers)
num_append(numbers)
print(numbers)


# 불변 타입 - 함수에 복사본이 넘어옴
# 정수, 실수, 문자열, 튜플


# 가변 타입 - 함수에 원본 그대로 넘어옴
# 리스트, 딕셔너리, set


def change_info(info):
    info["name"] = "이영희"
    info["age"] = 25


info_dic = {"name": "김철수", "age": 20}

print(info_dic)
change_info(info_dic)
print(info_dic)


# 실습3

current_user = None


def login(name):
    global current_user

    if current_user == None:
        current_user = name
        print(f"{name}님 로그인 성공")
    else:
        print("이미 로그인되어 있습니다.")


def logout():
    global current_user
    if current_user == None:
        print("로그인되어 있지 않습니다.")
    else:
        current_user = None
        print("로그아웃되었습니다.")


login("Ian")
login("Codingon")
logout()
logout()
login("Codingon")
print(current_user)
