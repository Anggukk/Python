import pandas as pd
import numpy as np

'''
# 실습1. 조건 필터링 연습

df = pd.DataFrame({
    "이름": ["민준", "서연", "지후", "서준", "지민"],
    "점수": [78, 92, 85, 60, 88],
    "반": [1, 2, 1, 2, 1]
})

# 1. 점수가 80점 이상인 학생만 추출
print("=== 1 ===")
df1 = df[df["점수"] >= 80]
print(df1)


# 2. 1반 학생들 중 점수가 85점 이상인 학생만 추출
print("=== 2 ===")
df2 = df[(df["반"] == 1) & (df["점수"] >= 85)]
print(df2)


# 3. 이름이 서연 또는 지민인 학생만 추출
print("=== 3 ===")
df3 = df[(df["이름"] == "서연") | (df["이름"] == "지민")]
print(df3)


# 4. 문제3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력
print("=== 4 ===")
df4 = df3.reset_index(drop=True)
print(df4)


# 5. 점수가 80점 미만이거나 2반인 학생만 추출
print("=== 5 ===")
df5 = df[(df["점수"] < 80) | (df["반"] == 2)]
print(df5)


# 6. 문제5의 결과에서 점수 컬럼이 70점 이상인 학생만 다시 추출하고, 인덱스 재정렬하여 출력
print("=== 6 ===")
df6 = df5.reset_index()
print(df6)
'''


'''
# 실습2. 행/열 추가,수정,삭제

df = pd.DataFrame({
    "이름": ["김철수", "이영희", "박민수"],
    "국어": [90, 80, 70]
})

# 1. 수학 점수를 새 열로 추가하세요.
print("=== 1 ===")
df1 = df
df1["수학"] = [95, 100, 88]
print(df1)


# 2. 1번 문제의 DataFrame에서 이름 열을 삭제하세요.
print("=== 2 ===")
df2 = df1.drop("이름", axis=1)
print(df2)


# =====================

df = pd.DataFrame({
    "제품": ["A", "B"],
    "가격": [1000, 2000]
})


# 3. 제품 C, 가격 1500인 새 행을 추가하세요.
print("=== 3 ===")
df3 = pd.DataFrame([{
    "제품": "C",
    "가격": 1500
}])
df = pd.concat([df, df3], ignore_index=True)
print(df)


# 4. 3번 문제의 DataFrame에서 첫 번째 행(제품"A")을 삭제하세요.
print("=== 4 ===")
df4 = df.drop(0)
print(df4)


# =====================

df = pd.DataFrame({
    "과목": ["국어", "영어", "수학"],
    "점수": [85, 90, 78]
})

# 5. 점수가 80 미만인 행을 모두 삭제하세요.
print("=== 5 ===")
df5 = df[df["점수"] >= 80]
print(df5)

df5 = df.drop(df[df["점수"] < 80].index)
print(df5)


# 6. 학년 열(값은 모두 1)을 추가하세요.
print("=== 6 ===")
df["학년"] = 1
print(df)


# =====================

df = pd.DataFrame({
    "이름": ["A", "B"],
    "나이": [20, 22]
})


# 7. 이름이 "C", 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
print("=== 7 ===")
df7 = pd.DataFrame({
    "이름": "C",
    "나이": 25,
    "키": NaN
})
df = pd.concat([df, df7], ignore_index=True)
print(df)
'''


'''
# 실습3. 정렬

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [88, 95, 70, 100]
})

# 1. score 기준 오름차순 정렬
print("=== 1 ===")
df1 = df.sort_values(by="score")
print(df1)

# 2. score 기준 내림차순 정렬, 0부터 재정렬
print("=== 2 ===")
df2 = df.sort_values(by="score", ascending=False)
df2 = df2.reset_index(drop=True)
print(df2)


# ================

df = pd.DataFrame({
    '이름': ['가', '나', '다', '라', '마'],
    '반': [2, 1, 1, 2, 1],
    '점수': [90, 85, 80, 95, 85]
})

# 3. 반 기준 오름차순, 같은 반 내에서는 점수 기준 내림차순 정렬
print("=== 3 ===")
df3 = df.sort_values(by=["반", "점수"], ascending=[True, False])
print(df3)


# 4. 열 이름을 알파벳순으로 정렬
print("=== 4 ===")
df4 = df.sort_index(axis=1)
print(df4)


# =================

df = pd.DataFrame({
    'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])

# 5. 인덱스 기준 오름차순 정렬
print("=== 5 ===")
df5 = df.sort_index()
print(df5)


# 6. 인덱스 기준 내림차순 정렬, value 기준 오름차순 정렬 각각 출력
print("=== 6 ===")
df61 = df.sort_index(ascending=False)
df62 = df.sort_values(by="value")
print(df61)
print(df62)
'''


'''
# 실습4. groupby 연습문제
# 1. 각 grade 별 평균 국어 점수
print("=== 1 ===")
df = pd.DataFrame({
    'grade': [1, 2, 1, 2, 1, 3],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
    'kor': [85, 78, 90, 92, 80, 75]
})

print(df.groupby("grade")["kor"].mean())


# 2. class별 subjict별로 시험에 응시하나 학생 수와 평균
print("=== 2 ===")
df = pd.DataFrame({
    'class': [1, 1, 1, 2, 2, 2],
    'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
    'score': [80, 90, 85, 70, 95, 90]
})

print(df.groupby("class")["score"].agg(["count", "mean"]))
print(df.groupby("subject")["score"].agg(["count", "mean"]))


# 3. 지역별 판매자 별로 판매액의 합계와 최대값
print("=== 3 ===")
df = pd.DataFrame({
    'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu'],
    'seller': ['A', 'B', 'A', 'B', 'A'],
    'sales': [100, 200, 150, 120, 130]
})

print(df.groupby("region")["sales"].agg(["sum", "max"]))
print(df.groupby("seller")["sales"].agg(["sum", "max"]))


# 4. 팀별, 포지션별로 결측치를 포함한 점수의 평균
print("=== 4 ===")
df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'A', 'B'],
    'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
    'score': [3, 2, None, 1, 4, 2]
})

print(df.fillna(0).groupby("team")["score"].mean())
print(df.fillna(0).groupby("position")["score"].mean())


# 5. 부서별로 성별별 인원수와 총 연봉 합계
print("=== 5 ===")
df = pd.DataFrame({
    'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
    'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})
print(df.groupby("dept")["gender"].count())
print(df.groupby("dept")["salary"].sum())
'''


missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})


# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})


employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})


# GroupBy 핵심
'''
Spllit - Apply - Combine
3단계 프로세스

1. Split (분할) - 데이터를 그룹으로 나누기
2. Apply (적용) - 각 그룹에 함수 적용
3. Combine (결합) - 결과를 하나로 합치기
'''


simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})

print(simple_data)


# 1단계 Split (분할)
for category, group in simple_data.groupby("category"):
    print(f"{category} 그룹")
    print(group)


# 2단계 Apply (적용)
for category, group in simple_data.groupby("category"):
    avg = group["value"].mean()
    print(f"{category} 그룹 평균 {avg}")


# 3단계 Combine (결합)
result = simple_data.groupby("category")["value"].mean()
print(result)
