import pandas as pd

# 샘플 데이터
data={
    "나이": [25,30,None,40,35],
    "연봉":[3000,4500,3500,None,4000],
    "이탈":["N","N","Y","N","Y"]
}
df=pd.DataFrame(data)

# 결측치 확인
print(df.isnull().sum())

# 결측치 처리(평균으로 대체)
df["나이"]=df["나이"].fillna(df["나이"].mean())
df["연봉"]=df["연봉"].fillna(df["연봉"].mean())

# 범주형 데이터 인코딩
df["이탈"]=df["이탈"].map({"N":0,"Y":1})

print(df)



from sklearn.linear_model import LogisticRegression


'''
# 모델 생성
model=LogisticRegression()

# 학습(fit)
model.fit(x_train,y_train)

# 예측(predict)
predictions=model.predict(x_train)

# 회귀 평가 지표
# - MSE (평균 제곱 오차)
# - RMSE (평균 제급근 오차)
# - MAE (평균 절대 오차)
# - R^2 (결정 계수)
'''