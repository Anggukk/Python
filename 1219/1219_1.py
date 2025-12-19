import pandas as pd
import numpy as np

df = pd.DataFrame({
    'age': [25, 30, np.nan, 45, np.nan, 35],
    'income': [50000, np.nan, 60000, 80000, 55000, np.nan],
    'city': ['서울', '부산', np.nan, '대구', '서울', '인천']
})

print("=== 결측치 확인 ===")
print(df.isnull().sum())


# 방법 1 : 삭제
# 결측치가 있는 행 전체를 삭제

df_drop=df.dropna()
print(f"원본 : {len(df)}행 => 삭제 후 : {len(df_drop)}행")


# 방법 2 : 채우기
# 수치형 : 평균/중앙값/최빈값으로 채우기
df["age"]=df["age"].fillna(df["age"].median()) #중앙값
df["income"]=df["income"].fillna(df["income"].mean()) #평균

print(df.isnull().sum())


# 매핑
# 방법 1 수동매핑
df=pd.DataFrame({
    "sex" : ["male","female","male","female"]
})

df["sex"]=df["sex"].map({"male":0,"female":1})
print(df)

# 방법 2 LabelEncoder
from sklearn.preprocessing import LabelEncoder

df=pd.DataFrame({
    "city":["서울","부산","대전","대구","서울","인천"]
})

le=LabelEncoder()
df["city_encoded"]=le.fit_transform(df["city"])

print(df)