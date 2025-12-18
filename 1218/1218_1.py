# import numpy as np
# import matplotlib.pyplot as plt


# # 한글 폰트 설정 추가
# plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# # plt.rcParams['font.family'] = 'AppleGothic'  # Mac
# plt.rcParams['axes.unicode_minus'] = False

# def sigmod(z):
#     return 1 / (1 + np.exp(-z))

# # 시각화
# z = np.linspace(-10, 10, 100)
# y = sigmod(z)

# plt.figure(figsize=(10, 6))
# plt.plot(z, y, 'b-', linewidth=2)
# plt.axhline(y=0.5, color='r', linestyle='--', label='경계 (0.5)')
# plt.axvline(x=0, color='gray', linestyle='-' ,alpha=0.3)
# plt.xlabel('z (wx + b)')
# plt.ylabel('σ(z)')
# plt.title('시그모이드 함수')
# plt.legend()
# plt.grid(True)
# plt.show()



# 과제
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. 데이터 로드 (CSV 파일 경로)
df=pd.read_csv("Titanic.csv",sep="\t")

# 2. 필요한 특성만 선택 (dropna())
df=df[["Survived","Sex","Age","Pclass","SibSp","Parch","Fare"]]
df=df.dropna()

# 3. 성별을 숫자로 변환
df["Sex"]=df["Sex"].map({"male":0,"female":1})

# 4. 특성과 타켓 분리
x=df[["Sex","Age","Pclass","SibSp","Parch","Fare"]]
y=df["Survived"]

# 5. 분할
x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

# 6. 모델 학습
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(x_train,y_train)

# 7.평가
pred=model.predict(x_test)
print("Accuracy : ",accuracy_score(y_test,pred))

# 8. 시각화
plt.figure(figsize=(10,6))
plot_tree(
    model,
    feature_names=x.columns,
    class_names=["Died","Survied"],
    filled=True,
    rounded=True,
    fontsize=12
)
plt.show()
