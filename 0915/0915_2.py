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
