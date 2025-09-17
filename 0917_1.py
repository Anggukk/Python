colors = ["red", "blue"]
fruits = ["apple", "banana"]

for color in colors:
    for fruit in fruits:
        print(f"{color}, {fruit}")


# break
for i in range(3):
    if i == 2:
        break
    print(i)

for i in range(10):
    print(i)
    break

print("for문 종료")


# continue - 밑에만 실행 안하고 반복문 그대로 진행
for i in range(10):
    if i % 2:
        continue
    print(i)


# for-else문 - for문이 전부 수행됐을 때 else문 실행
for i in range(10):
    print(i)
    if i == 4:
        break
else:
    print("루프 정상 종료")


'''
# 실습3
# 문제1
for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
    print()


# 문제2
n = int(input("몇 줄? > "))


# 왼쪽정렬
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()


# 가운데 정렬
star = n*2-1
blank = star//2

for i in range(n):
    for j in range(blank):
        print(" ", end="")
    for j in range(i*2+1):
        print("*", end="")
    for j in range(blank):
        print(" ", end="")
    print()
    blank -= 1


# 오른쪽 정렬

for i in range(n, 0, -1):
    for j in range(i-1):
        print(" ", end="")
    for j in range(n-i+1):
        print("*", end="")
    print()
'''


# 실습4
# 문제1
list2 = [x**2 for x in range(1, 11)]
print(list2)


# 문제2
list3 = [x for x in range(1, 51) if x % 3 == 0]
print(list3)


# 문제3
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

list5 = [x for x in fruits if len(x) >= 5]
print(list5)
