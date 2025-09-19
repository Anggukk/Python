# 재귀 함수(Recursive Function)
'''
재귀 함수는 자기 자신을 호출하는 함수
'''


# 팩토리얼 계산 (n! = n * (n-1) * ... * 2 * 1)
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)


print(factorial(5))


# 피보나치 수열
# 0 1 1 2 3 4 8 13 ...

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)


for i in range(10):
    print(fibonacci(i))


# 실습4
# 거듭 제곱
def square(a, b):
    if b == 0:
        return 1
    return a*square(a, b-1)


print(square(2, 6))


# 문자열 뒤집기
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1]+reverse_string(s[:-1])


print(reverse_string("hello"))


'''
# 실습5
# 팩토리얼
n = int(input("정수 n(팩토리얼) : "))
fac = 1

for i in range(1, n+1):
    fac *= i

print(fac)


# 팩토리얼 - 재귀함수
def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)


n = int(input("정수 n(팩토리얼) : "))
print(factorial(n))
'''


'''
# 실습6
# 피보나치 수열
fibo = 1

for i in range(1, n+1):
    fibo += fibo


n = 4
print(fibo)
'''


# 함다 함수(Lambda Function)
'''
람다 함수는 이름 없는 한 줄짜리 간단한 함수
'''


# 일반 함수
def square(x):
    return x**2


# 람다 함수
# square_lambda=lambda x : x**2


print(square(5))
# print(square_lambda(5))
print((lambda x: x**2)(5))


# map() : 모든 요소에 함수 적용
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print(squared)


def increment_fun(x):
    return x+1


incre_numbers = list(map(increment_fun, numbers))
print(incre_numbers)


# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# sorted() - 정렬 기준 지정

students = [
    {"name": "홍길동", "score": 80},
    {"name": "김철수", "score": 92},
    {"name": "이영희", "score": 72}
]

students.sort(key=lambda x: x["score"], reverse=True)
for student in students:
    print(f"{student["name"]} : {student["score"]}점")
