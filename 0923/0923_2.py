# 모듈
'''
파이썬 코드가 저장된 파일
함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있습니다.

도구상자 : 여러 도구(함수)를 모아둔 상자(모듈)
'''


# 코드 재사용 : 한 번 작성한 코드를 여러 곳에서 사용
# 유지 보수 : 기능별로 분리하여 관리가 쉬움
# 협업 : 팀원들과 코드 공유가 편리
# 네임스페이스 : 이름 충돌 방지


# 전체 모듈 가져오기
import calculator


# 작성 되어 있는 모듈


result = calculator.add(10, 5)
print(result)


# 실습1


print(calculator.add(5, 6))
print(calculator.subtract(10, 3))
print(calculator.multiply(4, 5))
print(calculator.divide(5, 4))

print(calculator.divide(5, 0))


# 가상환경
# 프로젝트별로 독립적인 패키지 환경을 만들 수 있다.


# pip
# 파이썬 패키지 관리자


# 가상 환경 생성
# python -m venv 이름(myenv)


# 가상 환경 활성화
# myenv/Scripts/activate
# source myenv/Scripts/activate


# 가상 환경 비활성화
# deactivate
