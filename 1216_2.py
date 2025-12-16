from sklearn.model_selection import train_test_split
import numpy as np

# 샘플 데이터
x=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20]])
y=np.array([0,0,0,1,1,0,1,1,0,1])

x_train, x_test, y_train, y_test=train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

print(f"훈련 데이터 : {len(x_train)}")
print(f"테스트 데이터 : {len(x_test)}")



# 계층 분할
# 불균형 데이터 예시
y=np.array([0,0,0,0,0,0,0,1,1,1])

# stratify 옵션 사용
x_train, x_test, y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print(f"전체 클래스 비율 : {np.bincount(y)}")
print(f"훈련 클래스 비율 : {np.bincount(y_train)}")
print(f"테스트 클래스 비율 : {np.bincount(y_test)}")


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# 붓꽃 데이터 로드
iris = load_iris()
X = iris.data       # 특성 (꽃잎, 꽃받침 크기)
y = iris.target     # 라벨 (품종)

print(f"전체 데이터: {X.shape}")
print(f"클래스: {np.unique(y)}")  # [0, 1, 2]

from sklearn.datasets import load_wine

wine=load_wine()
x,y=wine.data,wine.target

# 1. 훈련:테스트 = 70:30으로 분할
# 2. stratify 적용
# 3. 각 세트의 클래스 분포 확인

x_train, x_test, y_train,y_test=train_test_split(
    x,y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

print(f"전체 클래스 분포 : {np.bincount(y)}")
print(f"훈련 데이터 클래스 분포 : {np.bincount(y_train)}")
print(f"테스트 데이터 클래스 분포 : {np.bincount(y_test)}")
