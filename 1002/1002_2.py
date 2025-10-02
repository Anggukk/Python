# Data Frame
# Data Frame은 pandas의 핵심 자료구조로 2차원 표 형태의 데이터를 다루는 객체

'''
핵심 개념
2차원 구조 : 행, 열로 구성된 표
Series의 집합 : 여러 개의 Series가 열로 배치된 형태
레이블 기반 : 각 행과 열에 이름(레이블)을 붙일 수 있음
각 열마다 다른 데이터 타입 가능
'''

import pandas as pd

# Data Frame의 구성 요소
test_data = pd.DataFrame(
    # 1. 데이터 (Value) - 2차원 배열
    data=[
        ["김철수", 27, "Dev", 4500],
        ["이영희", 23, "Hr", 4800]
    ],
    # 2. 행 인덱스(index) -  각 행의 레이블
    index=["E001", "E002"],
    # 3. 열 이름 (columns) - 각 열의 레이블
    columns=["이름", "나이", "department", "salary"]
)
print("==== Data Frame ====")
print(test_data)


print("1. 행 인덱스 ", test_data.index.tolist())
print("2. 열 인덱스 ", test_data.columns.tolist())
print("3. 데이터 형태 ", test_data.shape)
print("4. 행 개수 ", test_data.shape[0])
print("5. 열 개수 ", test_data.shape[1])
print("6. 전체 셀 개수", test_data.size)


# 실습2. DataFrame 연습
# 1
d1 = pd.DataFrame(
    data=[
        ["홍길동", 28, "서울"],
        ["김철수", 33, "부산"],
        ["이영희", 25, "대구"]
    ],
    columns=["이름", "나이", "도시"]
)
print("문제1:")
print(d1)


# 2
d2 = pd.DataFrame(
    data={
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    }
)
print("문제2:")
print(d2)


# 3
d3 = pd.DataFrame(
    data=[
        {
            "과목": "수학",
            "점수": 90
        },
        {
            "과목": "영어",
            "점수": 85
        },
        {
            "과목": "과학",
            "점수": 95
        }
    ]
)
print("문제3:")
print(d3)


# 4
d4 = pd.DataFrame(
    data={
        "이름": ["민수", "영희", "철수"],
        "점수": [80, 92, 77]
    },
    index=["학생1", "학생2", "학생3"]
)
print("문제4:")
print(d4)


# 5
kor = pd.Series([90, 85, 80], index=["a", "b", "c"])
eng = pd.Series([95, 88, 82], index=["a", "b", "c"])

d5 = pd.DataFrame({"kor": kor, "eng": eng})
print("문제5:")
print(d5)


# 6
d6 = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})
print("문제6:")
print(d6[["B", "A"]])


# 7
d7 = pd.DataFrame([
    ["펜", 1000, 50],
    ["노트", 2000, 30]
])
d7.columns = ["product", "price", "stock"]
print("문제7:")
print(d7)


# 8
d8 = pd.DataFrame({
    "국가": ["한국", "일본", "미국"],
    "수도": ["서울", "도쿄", "워싱턴"]
})
print("문제8:")
print(d8[["국가"]])
