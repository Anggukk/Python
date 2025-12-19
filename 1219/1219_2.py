import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# 1단계 : 데이터 탐색(EDA)
# 데이터 불러오기
df=pd.read_csv("Titanic1.csv",sep="\t")

# 결측치 확인
print(df.isnull().sum())

# 생존/사망 비율 파악
# survival_rate=df["Survived"].mean()
# print(f"Survival rate : {survival_rate:.2f}")
print(df["Survived"].value_counts(normalize=True).round(4))

# 성별, 객실 등급별 생존율 시각화
sex_survival=df.groupby("Sex")["Survived"].mean()

plt.bar(sex_survival.index, sex_survival.values)
plt.title("Survival Rate by Sex")
plt.show()

class_survival=df.groupby("Pclass")["Survived"].mean()

plt.bar(class_survival.index.astype(str), class_survival.values)
plt.title("Survival Rate by Class")
plt.show()

# 특성 간 상관관계 히트맵 그리기
numeric_df=df.select_dtypes(include="number")
corr=numeric_df.corr()

plt.imshow(corr)
plt.xticks(range(len(corr.columns)),corr.columns,rotation=45)
plt.yticks(range(len(corr.columns)),corr.columns)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()


# 2단계 데이터 전처리
# 필요한 특성만 선택
df=df[["Survived","Sex","Age","Pclass","Fare","SibSp","Parch"]]

# 결측치 채우기
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Fare"]=df["Fare"].fillna(df["Fare"].mean())

# 범주형 데이터를 숫자로 변환
df["Sex"]=df["Sex"].map({"male":0,"female":1})

# 훈련/ 테스트 세트 분할
from sklearn.model_selection import train_test_split

# X=df[["Sex","Age","Pclass","SibSp","Parch","Fare"]]
# y=df["Survived"]
X=df.drop("Survived",axis=1)
y=df["Survived"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)


# 3단계 모델 학습 및 비교
# 3가지 모델 훈련: 로지스틱 회귀, 결정 트리, 랜덤 포레스트
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

log_reg=LogisticRegression(max_iter=1000)
tree=DecisionTreeClassifier()
forest=RandomForestClassifier()

log_reg.fit(X_train,y_train)
tree.fit(X_train,y_train)
forest.fit(X_train,y_train)

print("LogReg train acc : ",log_reg.score(X_train,y_train))
print("DecisionTree train acc : ",tree.score(X_train,y_train))
print("RandomForest train acc : ",forest.score(X_train,y_train))

# 교차 검증로 성능 비교
from sklearn.model_selection import cross_val_score

log_scores=cross_val_score(log_reg,X_train,y_train,cv=5)
tree_scores=cross_val_score(tree,X_train,y_train,cv=5)
forest_scores=cross_val_score(forest,X_train,y_train,cv=5)

print("LogReg CV mean : ",log_scores.mean())
print("DecisionTree CV mean : ",tree_scores.mean())
print("RandomForest CV mean : ",forest_scores.mean())

# GridSearchCV로 랜덤 포레스트 하이퍼파라미터 튜닝
from sklearn.model_selection import GridSearchCV

param_grid={
    "n_estimators":[50,100,200],
    "max_depth":[None,5,10,15],
    "min_samples_split":[2,5,10]
}

grid_search=GridSearchCV(
    estimator=forest,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train,y_train)
print("Best parameters : ",grid_search.best_params_)
print("Best score : ",grid_search.best_score_)