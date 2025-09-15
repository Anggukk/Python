# 집합(set)


'''
# 리스트로 중복 제거 (비효율적)
unique_vistors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:
        unique_visitors_list.append(visitor)



# Set으로 중복 제거 (효율적)
unique_visitors_set = set(visitors)
print(unique_visitors_list)
'''


# 특징
# 1. 순서 없음: 요소들의 순서가 보장 되지 않음
# 2. 중복 불가 : 같은 값은 하나만 저장
# 3. 변경 가능 : 요소 추가 / 삭제 가능
# 4. 인덱싱 불가 : 순서가 없어 인덱스로 접근 불가
# 5. 빠른 검색 0(1)시간 복잡도로 요소 확인


# set 생성 방법
# 1. 빈 set 생성
empty_set = set()

# 2. 값이 있는 set 생성
numbers = {1, 2, 3, 5, 4, 3, 2, 4, }
fruits = {"사과", "바나나", "오렌지"}

# 3. 리스트 / 튜플에서 set 생성
list_numbers = [1, 2, 3, 4, 5, 6, 7]
set_numbers = set(list_numbers)
print(set_numbers)


# Comprehension
for i in range(10):
    print(i)


com_set = {i for i in range(10)}
print(com_set)


com_list = [i for i in range(2, 10, 2)]
print(com_list)


# set에 저장 가능한 데이터 타입
# Hashable 타입만 가능 (불변 타입)
valid_set = {1, "문자열", (1, 2), 3.14, True, }


'''
# Unhashable 타입 불가능 (가변 타입)
invalid_set = {[1, 2], {"key": "value"}, {1, 2}}
'''


# 중첩 set을 만드려면 frozenset() 사용
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)


# set 메서드
colors = {"빨강", "노랑", "파랑"}

colors.add("초록")
print(colors)

colors.add("초록")
print(colors)

colors.update(["보라", "주황"])
print(colors)

colors.update(["검정"], {"하양", "회색"})
print(colors)

colors.remove("검정")
print(colors)

colors.discard("검정")  # Error 안나는 삭제 명령어
print(colors)

popped = colors.pop()
print(popped)

colors.clear()
print(colors)


# 집합 연산
A = {1, 2, 3, 4, 5}
B = {1, 2, 6, 7, 8, }


# 교집합
intersection1 = A & B
intersection2 = A.intersection(B)

print(intersection1)
print(intersection2)


# 합집합
union1 = A | B
union2 = A.union(B)

print(union1)
print(union2)


# 차집합(Difference)
defference1 = A-B
defference2 = A.difference(B)

print(defference1)
print(defference2)


# 대칭 차집합(Symmetric Difference)(합집합-교집합)
sym_diff1 = A ^ B
sym_diff2 = A.symmetric_difference(B)

print(sym_diff1)
print(sym_diff2)


A = {1, 2, 3}
B = {3, 4, 5}

A.intersection_update(B)  # A를 A와B의 교집합으로 업데이트
# A &= B
print(A)


A = {1, 2, 3}
A.difference_update(B)  # A를 A와B의 차집합으로 업데이트
# A -= B
print(A)


A = {1, 2, 3}
A.symmetric_difference_update(B)  # A를 대칭차집합으로 업데이트
# A ^= B
print(A)


A = {1, 2, 3}
A.update(B)  # 합집합으로 업데이트
# A |= B
print(A)


# 집합 관계 확인
# 부분집합, 상위집합


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}


# 부분집합인지 확인
print(A.issubset(B))
print(A <= B)

print(B.issubset(A))


# 상위 집합인지 확인
print(A.issuperset(B))

print(B.issuperset(A))
print(A <= B)


# 진부분집합 확인
print(B > A)
print(B < A)


# 서로수 집합 - 교집합이 없는지 확인
print(A.isdisjoint(C))


# frozenset() - 불변 집합
fs1 = frozenset([1, 2, 3, 3, 4])

# fs1.add(5)  # 불변이므로 수정 불가
# fs1.remove()
# fs1.discard()


# 실습1
# 문제1

submissions = ["kim", "lee", "kim", "park", "choi", "lee", "lee"]

set_submissions = set(submissions)

print(f"""제출한 학생 수 : {len(set_submissions)}
제출자 명단 : {set_submissions}""")


# 문제2

user1 = {"SF", "Action", "Drama"}
user2 = {"Drama", "Romance", "Action"}

print(f"""공통 관심 장르 : {user1 & user2}
서로 다른 장르 : {user1 ^ user2}
전체 장르 : {user1 | user2}""")


# 문제3

my_certificates = {"SQL", "Python", "Linux"}
job_required = {"SQL", "Python"}

print(f"지원 자격 충족 여부 : {my_certificates >= job_required}")
