# Stack
'''
스택(stack) 후입선출(LIFO) 원칙을 따르는 선형 자료구조
가장 나중에 들어간 데이터가 가장 먼저 나오는 구조 -> 책을 쌓아놓는 것과 같은 형태
스택은 한쪽 끝 (top)에서만 데이터의 삽입과 삭제가 일어난다.
'''

# 핵심 특징
'''
1. LIFO(Last In First Out)
    가장 최근에 추가된 요소가 가장 먼저 제거
2. 제한된 접근
    스택의 요소들은 오직 Top을 통해서만 접근 가능합니다.
    중간 요소에 직접 접근할 수 없습니다.
3. 주요 연상의 0(1) 시간 복잡도
    push(삽입)와 pop(삭제) 연산 모두 0(1)의 시간 복잡도를 가집니다.
4. 메모리 효율성
    동적 배열이나 연결 리스트로 구현 가능하며, 필요에 따라 크기를 조절 할 수 있다.
'''


'''
push(data) : 스택의 맨 위에 요소 추가
pop() : 스택의 맨 위 요소 제거 및 반환
peek()/top() : 맨 위 요소 확인 (제거하지 않음)
is_empty() : 스택이 비어있는지 확인
size() : 스택의 요소 개수 반환
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self, items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f"스택 : {stack}")


# 큐(Queue)
'''
큐(Queue)는 선입선출(FIFO) 원칙을 따르는 선형 자료 구조
가장 먼저 들어간 데이터가 가장 먼저 나오는 구조 -> 줄 서기 형태
큐는 한쪽 끝

1. 
2.
3. 순차적 처리
    작업들을 순서대로 처리해야 할 때 유용합니다.
4. 공평한 자원 분배
    먼저 요청한 작업이 먼저 처리되는 공정성을 보장합니다.
'''


'''
class ListQueue:
    def __init__():

    def inqueue(self):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return 
        raise IndexError("Queue is empty")

    def front(self):
        if not s
'''


# 파일 입출력
'''
파일 입출력(File I/O)은 프로그램이 파일을 읽고(input) 쓰는(output) 작업입니다.
프로그램이 종료되어도 데이터를 보관할 수 있는 유일한 방법
프로그램의 데이터는 메모리에 저장되는데 프로그램이 종료되면 메모리의 데이터는 사라집니다.
파일로 저장하면 하드디스크에 영구 보관됩니다.
'''


# 파일 입출력이 필요한 상황
'''
1. 설정 파일 저장 : 게임 설정, 프로그램 옵션
2. 데이터 백업 : 중요한 정보 보관
3. 로그 기록 : 프로그램 실행 기록, 에러 추적
4. 데이터 교환 : 엑셀, csv 파일로 다른 프로그램과 데이터 공유
5. 데이터 처리 : 메모리에 다 못 담는 빅데이터 처리
'''


# 1단계: 파일 열기 (open) - 파일과 연결 통로 생성
file = open("data.txt", "r", encoding="utf-8")

# 2단계 : 파일 작업 (read/Write) - 데이터 읽기/쓰기
content = file.read()
print(content)

# 3단계 : 파일 닫기 (Close) - 연결 종료
file.close()


# 안전한 방법 2 - with문 (권장!)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# 자동으로 close() 됨

# 새 파일 생성 또는 덮어쓰기
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("파이썬 파일 입출력\n")

with open("output.txt", "a", encoding="utf-8") as f:
    f.write("추가된 내용\n")


# 1. read() - 파일 전체를 하나의 문자열로
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# read(크기) - 저장한 크기만큼만
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read(3)
    print(content)


# 2. readline() - 한 줄씩 읽기
print("readline() - 한 줄씩 읽기")
with open("data.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip())  # 공백, 탭, 줄바꿈 양쪽 제거
    print(line2.strip())


# readlines()
print("readlines()")
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # ["첫줄\n", "둘째줄\n" , "셋째줄\n"]

    for line in lines:
        print(line.strip())


'''
# 실습1. 회원 명부 작성하기
x1, y1 = input("회원 이름 / 비밀번호 : ").split("/")
x2, y2 = input("회원 이름 / 비밀번호 : ").split("/")
x3, y3 = input("회원 이름 / 비밀번호 : ").split("/")


with open("member.txt", "w", encoding="utf-8") as f:
    f.write(f"{x1}/{y1}\n")
    f.write(f"{x2}/{y2}\n")
    f.write(f"{x3}/{y3}\n")

with open("member.txt", "r", encoding="utf-8") as f:
    members = f.readlines()  # ["첫줄\n", "둘째줄\n" , "셋째줄\n"]

    for member in members:
        print(member.strip())


# 실습2. 회원 명부를 이용한 로그인 기능
name = input("이름을 입력하세요.")
password = input("비밀번호를 입력하세요.")

with open("member.txt", "r", encoding="utf-8") as f:
    members = f.readlines()  # ["첫줄\n", "둘째줄\n" , "셋째줄\n"]

found = False
for member in members:
    member = member.strip()
    member_name, member_pw = member.split("/")
    if name == member_name and password == member_pw:
        print("로그인 성공!")
        found = True
        break

if not found:
    print("로그인 실패")
'''


'''
# 문제1 : 나이 입력 프로그램
def get_age_group():
    try:
        age = int(input("나이를 입력하세요 : "))
    except ValueError:
        print("숫자로 입력해주세요.")
        age = int(input("나이를 입력하세요 : "))
    if 0 <= age < 20:
        print("미성년자")
    elif 20 <= age < 40:
        print("청년")
    elif 40 <= age < 60:
        print("중년")
    elif 60 <= age < 150:
        print("노년")
    else:
        print("에러")


get_age_group()
'''


# 문제2 : 리스트 안전 접근
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default


numbers = [10, 20, 30]

print(safe_get(numbers, 1))
print(safe_get(numbers, 10))
print(safe_get(numbers, 10, -1))
