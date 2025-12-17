import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([2,4,5,4,5])

# 평균
x_mean=np.mean(x)
y_mean=np.mean(y)

# 최소제곱법
numerator=np.sum((x-x_mean)*(y-y_mean))
denominator=np.sum((x-x_mean)**2)

w=numerator/denominator
b=y_mean-w*x_mean

print(f"기울기 (w) : {w:.4f}")
print(f"절편 (b) : {b:.4f}")
print(f"예측식 y= {w:.2f}x + {b:.2f}")


# 모델 생성 및 학습
from sklearn.linear_model import LinearRegression

x_2d=x.reshape(-1,1)

model=LinearRegression()
model.fit(x_2d,y)

# 파라미터 확인
print(f"기울기 : {model.coef_[0]:.4f}")
print(f"절편 : {model.intercept_:.4f}")

# 예측
y_pred=model.predict(x_2d)
print(f"예측값 : {y_pred}")

# # 시각화
# import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우 기본 한글 폰트
# plt.rcParams['axes.unicode_minus'] = False

# plt.figure(figsize=(10,6))

# # 데이터 점
# plt.scatter(x, y, color='blue', s=100, label='실제데이터')

# # 회귀선
# plt.plot(x, y_pred, color='red', linewidth=2, label='회귀선')

# # 오차 시각화
# for i in range(len(x)):
#     plt.plot([x[i],x[i]], [y[i],y_pred[i]], 'g--', alpha=0.5 )


# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('선형 회귀')
# plt.legend()
# plt.grid(True)
# plt.show()



# 실습 과제
print("=== 실습 과제 ===")

광고비=np.array([1,2,3,4,5,6,7,8,9,10])
매출=np.array([3,5,6,8,11,13,14,16,17,20])

# 1. 선형 회귀 모델 학습
# 2. 기울기와 절편 확인
# 3. 광고비 15이상일 때 예상 매출 예측
# 4.R^2 Score 계산

x=광고비.reshape(-1,1)
y=매출

model=LinearRegression()
model.fit(x,y)

print(f"기울기 : {model.coef_[0]:.4f}")
print(f"절편 : {model.intercept_:.4f}")

예측_광고비=np.array([[15]])
예상_매출=model.predict(예측_광고비)

print(f"광고비 15일 때 예상 매출 : {예상_매출[0]:.2f}")

from sklearn.metrics import r2_score

y_pred=model.predict(x)
r2=r2_score(y,y_pred)

print(f"R² Score : {r2:.4f}")

r2=model.score(x,y)
print(f"R² Score : {r2:.4f}")