import numpy as np
import pandas as pd

# CSV 파일 예시 내용

'''
name,   age,    city,   salary
John,   25,     Seoul,  50000
Jane,   39,     Busan,  60000
Park,   35,     Daegu,  55000
'''


# df = pd.read_csv("sample_data.csv")
# print(df)

sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 55000]
})


# UTF-8로 저장 (기본값, 권장)
sample_data.to_csv("sample_data.csv", index=False, encoding="utf-8-sig")


# CP949로 저장 (Window 한글)
# sample_data.to_csv("sample_data.csv", index=False, encoding="cp949")


df = pd.read_csv("sample_data.csv")

print("=== CSV 파일 읽기 ===")
print(df)

print("=== 데이터 타입 ===")
print(df.dtypes)

print("데이터 크기 : ", df.shape)


# seq - 구분자 설정
sample_data.to_csv("tab_separated.txt", sep="\t", index=False)

df_tab = pd.read_csv("tab_separated.txt", sep="\t")

print("=== CSV sep=탭 파일 읽기 ===")
print(df_tab)
print(df_tab.head())    # 처음 5개 행 (기본값)


sample_data.to_excel("sample_data.xlsx", index=False, sheet_name="Defalt")
df_excel = pd.read_excel("sample_data.xlsx")
print("=== Excel 파일 읽기 ===")
print(df_excel)


# 여러 시트 다루기
with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    sample_data.to_excel(writer, sheet_name="Default1", index=False)
    sample_data["name"].to_excel(writer, sheet_name="name", index=False)

print("2개의 시트를 가진 엑셀 파일 생성 완료")


# JSON
# JSON(JavaScript Object Notation)
# 웹에서 많이 사용되는 데이터 형식


sample_data.to_json("sample_data.json", orient="records", indent=2)

print("JSON 파일 저장")


# 문제1
# 다음 데이터를 CSV로 저장하고 다시 읽어오세요

practice_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

# TODO:
# 1. 'practice.csv'로 저장 (인덱스 제외)
# 2. 저장한 파일 읽어오기
# 3. 읽어온 데이터 출력


practice_data.to_csv("practice.csv", index=False)
df = pd.read_csv("practice.csv")
print(df)


# 문제2
# 한글 데이터를 UTF-8로 저장하고 읽어오세요

korean_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '직급': ['사원', '대리', '과장']
})

# TODO:
# 1. UTF-8 인코딩으로 저장
# 2. 같은 인코딩으로 읽어오기
# 3. 한글이 깨지지 않았는지 확인

korean_data.to_csv("korean_data.csv", index=False)
df = pd.read_csv("korean_data.csv")
print(df)


# 실습4. 통계함수/결측값 처리 연습

data = {

    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],

    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],

    "초미세먼지": [20, np.nan, 17, 18, 22, 19],

    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]

}

df = pd.DataFrame(data)


# 1
print("미세먼지 평균 : ", df["미세먼지"].mean())
print("미세먼지 중앙값 : ", df["미세먼지"].median())


# 2
print("초미세먼지 최댓값 : ", df["초미세먼지"].max())
print("초미세먼지 최솟값 : ", df["초미세먼지"].min())


# 3
print("각 컬럼별 결측값 개수 : ")
print(df.isnull().sum())


# 4
df4 = df.dropna(axis=0, how="any", inplace=False)
print("남은 초미세먼지 평균 : ", df4["초미세먼지"].mean())
print("=== df4 ===")
print(df4)
print("=== 원본 df ===")
print(df)


# 5
df5 = df.fillna(0, method=None, inplace=False)
print("5번 미세먼지 합계 : ", df5["미세먼지"].sum())
print("5번 초미세먼지 합계 : ", df5["초미세먼지"].sum())


# 6
df_mean = df["미세먼지"].fillna(df["미세먼지"].mean())
print("미세먼지 표준편차 : ", df_mean.std())
