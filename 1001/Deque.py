# 덱(Deque)
'''
덱(Deque, Double_Ended Queue)
양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조

스택과 큐의 특성을 모두 가지고 있어, 매우 유연한 자료구조
'deck'으로 발음
'''

'''
특징
1. 양방향 연산 (Double_ended)
    앞쪽(front) 뒤쪽(rear) 모두에서 요소 추가 제거가 가능하다
2. O(1) 시간 복잡도
    양쪽 끝에서의 모든 연산이 상수 시간에 수행된다
3. 동적 크기
    필요에 따라 크기가 자동으로 조절
4. 스택과 큐 동시 구현
    하나의 자료구조로 스택과 큐를 모두 구현할 수 있다
5. 회전 연산 지원
    요소들을 좌우로 회전시킬 수 있다
'''

'''
주요 연산
append(x)       오른쪽 끝에 요소 추가
appendleft(x)   왼쪽 끝에 요소 추가

pop()           오른쪽 끝 요소 제거 및 반환
popleft()       왼쪽 끝 요소 제거 및 반환

extend(iterable)        오른쪽에 여러 요소 추가
extendleft(iterable)    왼쪽에 여러 요소 추가

rotate(n)       n만큼 회전
clear()         모든 요소 제거
'''


'''
회문(palindrome) 검사
level -> 좌우가 똑같은 단어
'''


from collections import deque
def is_palindrome(s):
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print(is_palindrome("level"))  # True
print(is_palindrome("tomato"))  # False
