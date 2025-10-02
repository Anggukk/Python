import pandas as pd

print(pd.__version__)

# 데이터 분석
# 과정
# 데이터 수집 -> 데이터 정제
# 데이터 탐색 -> 데이터 분석 -> 시각화
# 인사이트 도출


# Series
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name="4월 기온")
print(temp)

date = pd.date_range("2025-04-01", periods=5)
print(date)


temp_date = pd.Series(temp_list, index=date, name="4월 기온")
print(temp_date)


# 실습1.Series 연습
# 1
list = [5, 10, 15, 20]
s1 = pd.Series(list)
print("문제1:")
print(s1)


# 2
s2 = pd.Series([90, 80, 85, 70], index=["국어", "영어", "수학", "과학"])
print("문제2:")
print(s2)


# 3
dict3 = {
    "서울": 950,
    "부산": 340,
    "인천": 520
}
s3 = pd.Series(dict3)
print("문제3:", s3["인천"])


# 4
s4 = pd.Series([1, 2, 3, 4])
print("문제4:", s4.dtype)


# 5
s1 = pd.Series([3, 5, 7], index=["a,", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])
print("문제5:")
print(s1+s2)


# 6
s6 = pd.Series([1, 2, 3, 4, 5])
s6 = s6+10
print("문제6:")
print(s6)


# Series
# Pandas의 가장 기본되는 1차원 데이터 구조
'''
1. 1차원 배열 : 데이터가 일렬로 나열되어 있습니다.
2. 레이블(인덱스) 보유 : 각 데이터에 이름표를 붙일 수 있습니다.
3. 동일 타입 : 하나의 series 안의 모든 데이터는 같은 타입
'''


simple_series = pd.Series([10, 20, 30, 40, 50])
print(simple_series)


# Series = Value(값) + Indes(인덱스) + Name(이름)


data_series = pd.Series(
    data=[10, 20, 30, 40, 50],
    index=["Alice", "Bob", "Charlie", "David", "Lisa"],
    name="Test_Score"
)


# 인덱싱과 슬라이싱

# 인덱싱
# Series에서 특정 데이터를 선택하는 방법
# 위치 기반 0,1,2
# 레이블 기반 : 인덱스 이름으로 접근

sales = pd.Series(
    [100, 200, 150, 300],
    index=["Mon", "Tue", "Wed", "Thu"],
    name="Daily_Sales"
)
wed_sales = sales["Wed"]
print("수요일 매출 : ", wed_sales)


selected_days = sales[["Mon", "Wed", "Thu"]]
print(selected_days)


# 슬라이싱
print(sales.loc[:"Wed"])
print(sales[:"Wed"])


# Boolean 인덱싱
condition = sales >= 200
print(condition)
print()

result = sales[condition]
print(result)
print()


# 비교 연산자
print("sales[sales == 200]")
print(sales[sales == 200])
print()

print("sales[(sales>150)&(sales<=350)]")
print(sales[(sales >= 150) & (sales <= 350)])
print()


# 복합 조건
sales = pd.Series(
    [100, 200, 150, 300, 250],
    index=["Mon", "Tue", "Wed", "Thu", "Fri"],
    name="Daily_Sales"
)

weekday_high = sales[(sales >= 200) & (sales.index != "Fri")]


print("weekday_high")
print(weekday_high)
print()


weeked_or_low = sales[(sales < 200) | sales.index.isin(["Mon", "Fri"])]
print(weeked_or_low)
print()


# 벡터화 연산
prices = pd.Series(
    [3000, 1500, 4000, 2000],
    index=["apple", "banana", "orange", "grape"],
    name="Price"
)
print(prices+500)
print()


'''
# Nan 결측값 처리하며 연산하기
# 1. fill value 사용
price_diff_filled = store_b.sub(store_a, fill_value=0)
print("price_diff_filled")
print(price_diff_filled)
print()



# 2. reindex로 먼저 맞추기
store_a_reindexed = store_a.reindex(store_b.index, fill_value=0)
print(store_a_reindexed)
price_diff_reindexed = store_b-store_a_reindexed




# 3. drop
'''


# 통계 함수
# 데이터의 특징을 숫자로 요약하는 것


daily_sales = pd.Series(
    [
        302, 423, 123, 437, 890,
        124, 781, 920, 478, 901,
        241, 891, 123, 678, 912,
        165, 834, 453, 864, 434,
        344, 673, 654, 274, 341,
        967, 456, 100, 134, 341
    ],
    index=pd.date_range("2025-09-01", periods=30),
    name="Sales"
)
# 평균(mean) : 모든 값의 합 / 게수
mean_value = daily_sales.mean()
print(f"1. 평균 (Mean) : {mean_value}")


# 중앙값(Median) : 정렬했을 때 가운데 값
median_value = daily_sales.median()
print(f"2. 중앙값 (Median) : {median_value}")


# 최빈값 (mode) : 가장 자주 나타나는 값
mode_value = daily_sales.mode()
print(f"3. 최빈값 (Mode) : \n{mode_value}")


# 산포도 측정
