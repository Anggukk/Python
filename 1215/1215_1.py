import numpy as np

# 벡터
# 실습 과제

a=np.array([2,4,6])
b=np.array([1,4,5])

print("1. a + b = ",a+b)
print("2. a - b = ",a-b)
print("3. a * 3 = ",a*3)
print("4. a의 크기(노름) 계산 : ",(np.linalg.norm(a)))
print("5. a의 단위 벡터 구하기 : ",a/(np.linalg.norm(a)))





# 실습 과제

A=np.array([[1,2],[3,4],[5,6]])
B=np.array([[1,2,3],[4,5,6]])

print(A)
print(B)

print("1. A의 shape : ",np.shape(A))
print("2. A의 전치 행렬 : \n",np.transpose(A))
print("3. A @ B 계산 : \n",A@B)
print("4. B @ A 계산 : \n",B@A)
print("5. np.arange(12)를 3x4 행렬로 reshape : \n",np.reshape(np.arange(12),(3,4)))