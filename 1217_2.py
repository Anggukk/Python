from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 1. 데이터 준비
housing = fetch_california_housing()

x = housing.data
y = housing.target
feature_names = housing.feature_names

# 2. 데이터 확인
df = pd.DataFrame(x, columns=feature_names)
df['Target'] = y

print('데이터 크기:',x.shape)
print(df.describe())

# 3. 학습/테스트 분할
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

# X. 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# 4. 다중 선형 회귀 모델 학습
model=LinearRegression()
model.fit(x_train_scaled,y_train)

# 5. R² Score 확인
from sklearn.metrics import r2_score

y_pred=model.predict(x_test_scaled)
r2=r2_score(y_test,y_pred)

print(f"R² Score : {r2:.4f}")

# 6. 각 특성의 중요도 분석
importance = pd.Series(
    model.coef_,
    index=feature_names
).sort_values(ascending=False)

print(importance)