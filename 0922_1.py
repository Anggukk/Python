# 클래스
'''
클래스는 객체를 만들기 위한 설계도 입니다.
클래스 = 붕어빵 틀
객체(인스턴스) = 실제로 만들어진 붕어빵

클래스를 사용하면 관련된 데이터와 기능을 하나로 묶어서 관리
'''


'''
코드 재사용성 : 한번 작성한 코드를 여러 곳에서 활용
유지보수 용이 : 수정사항이 있을 때 클래스만 수정하면 됨
코드 구조화 : 복잡한 프로그램을 체계적으로 구성
현실 세계 모델링 : 실제 사물이나 개념을 프로그램으로 표현
'''


'''
class 클래스 이름:
    def __init__(self):
        pass

    def 메서드이름(self):
        pass
'''


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def acclerate(self, increase):
        self.speed = min(150, self.speed+increase)  # 속도가 150을 넘지 않도록 작성
        print(f"속도가 {increase}km/h 증가했습니다. 현재 속도 : {self.speed}km/h")

    def brake(self, decrease):
        self.speed = max(0, self.speed-decrease)  # 값이 0미만이 될 수 없도록 작성
        print(f"속도가 {decrease}km/h 감소했습니다. 현재 속도 : {self.speed}km/h")

    def info(self):
        print(f"브랜드 : {self.brand}")
        print(f"모델명 : {self.model}")
        print(f"색상 : {self.color}")
        print(f"현재 속도 : {self.speed}km/h")


# 객체 생성 및 사용
my_car = Car("tesla", "model 3", "빨간색")

# 객체 정보 출력
my_car.info()
my_car.acclerate(80)
my_car.brake(30)
my_car.info()


'''
# 실습1
# 문제1
class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        if pages < 0:
            return

        self.current_page = min(self.total_pages, self.current_page+pages)

    def progress(self):
        pct = (self.current_page/self.total_pages)*100
        print(round(pct, 1))


my_book = Book("파이썬 클린코드", "홍길동", 320, 0)
my_book.read_page(100)
print(my_book)
print(my_book.progress())
my_book.read_page(1000)
print(my_book.progress())
'''


'''
# 문제2
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


w, h = map(int, input("가로,세로 : ").split())
a = Rectangle(w, h)
print(a.area())
'''


'''
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []  # 성적 리스트 초기화
        print(f"학생 {name}의 정보가 등록 되었습니다.")

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name}의 성적 {grade}점이 추가 되었습니다.")

    def get_average(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0

    def __del__(self):
        print(f"{self.name}의 정보가 삭제 되었습니다.")


student1 = Student("김철수", 20, "20250001")
student1.add_grade(70)
student1.add_grade(60)
print(student1.get_average())

student2 = Student("이영희", 22, "20250002")
del student2
'''


# 인스턴스 변수, 클래스 변수
'''
인스턴스 변수 : 각 객체마다 독립적으로 가지는 변수
클래스 변수 : 모든 객체가 공유하는 변수
'''


class BankAccount:
    bank_name = "파이썬 은행"
    total_accounts = 0
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 잔액
        self.accout_number = BankAccount.total_accounts + 1

        BankAccount.total_accounts += 1  # 클래스 변수 업데이트

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금 되었습니다. 잔액 : {self.balance}원")
        else:
            print("입금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amout}원이 출금 되었습니다. 잔액 : {self.balance}원")
        else:
            print("잔액이 부족합니다.")

    def apply_interest(self):
        interest = self.balance*BankAccount.interest_rate
        self.balance += interest
        print(f"이자 {interest}원이 적용되었습니다. 잔액 : {self.balance}원")

    @classmethod
    def change_interest_rate(cls, new_rate):
        '''클래스 메서드'''
        cls.interest_rate = new_rate
        print(f"이자율 {new_rate*100}%로 변경 되었습니다.")

    def __del__(self):
        print(f"{self.owner}님 계좌를 삭제 했습니다.")
        BankAccount.total_accounts -= 1


accout1 = BankAccount("홍길동", 10000)
accout2 = BankAccount("김철수", 15000)

print(f"은행 이름 : {BankAccount.bank_name}")
print(f"총 계좌 수 : {BankAccount.total_accounts}")

accout1.deposit(50000)
accout2.apply_interest()  # 이자 적용

BankAccount.change_interest_rate(0.03)  # 이자 변경
accout1.apply_interest()  # 이자 적용


class Calculator:
    calculation_count = 0

    def __init__(self, name):
        self.name = name
        self.history = []

    # 인스턴스 메서드
    def add_to_history(self, operation, result):
        '''계산 기록 저장'''
        self.history.append(f"{operation}={result}")
        Calculator.calculation_count += 1

    # 클래스 메서드
    @classmethod
    def get_total_calculation(cls):
        '''전체 계산 횟수 반환'''
        return cls.calculation_count

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def is_even(number):
        return number % 2 == 0  # 불리언(True or False)

    def calculate_and_save(self, a, b, operation):
        if operation == "add":
            result = self.add(a, b)
            self.add_to_history(f"{a}+{b}", result)
        elif operation == "multiply":
            result = self.multiply(a, b)
            self.add_to_history(f"{a}*{b}", result)
        return result


calc1 = Calculator("계산기1")
calc2 = Calculator("계산기2")

print(Calculator.add(5, 3))
print(Calculator.is_even(5))

result = calc1.calculate_and_save(10, 20, "add")
print(f"경과 : {result}")

print(f"총 계산 횟수 : {Calculator.get_total_calculation()}")


# 실습2
# 문제1
class User:

    total_users = 0

    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount
        print(f"포인트 추가 {amount}점")

    def get_level(self):
        if 0 <= self.points < 100:
            return "Bronze"
        elif self.points < 500:
            return "Silver"
        else:
            return "Gold"

    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수 : {User.total_users}")

    def __del__(self):
        User.total_users -= 1


user1 = User("정은경", 50)
user2 = User("홍길동", 600)
user1.add_points(400)
print(user1.get_level())

User.get_total_users()


# 접근 제어자
'''
객체 지향 프로그래밍에서 클래스의 멤버(속성,메서드)에 대한 접근 권한을 제어하는 메커니즘

Python의 철학 : Python은 프로그래머를 신뢰하는 철학을 가짐
강제적 제한보다는 컨벤션과 문서화를 중시
필요하다면 모든것에 접근 가능(하지만 하지 말아야 할 것을 명확히 표시)
'''


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        return (f"속도가 {self.speed}km/h가 되었습니다.")

    def get_info(self):
        return f"{self.brand} {self.model}"


car = Car("tesla", "model 3")
print(car.model)
print(car.brand)
print(car.get_info())
car.speed = 200


'''
# Private 속성/메서드(언더스코어 2개 __)
class SecuritySystem:
    def __init__(self, password):
        self.__password = password  # private 속성
        self.__security_level = "HIGH"  # private 속성
        self.__failed_attempts = 0  # private 속성

    def __encrypt_password(self, pwd):  # private 메서드
        return pwd+"encrypted"

    def __check_security(self):
        return self.__failed_attempts < 3

    def authenticate(self, password):  # public 메서드
        if not self.__check_security():
            return "계정이 잠겼습니다."
        encrypted = self.__encrypt_password(self, password)
        if encrypted == self.__encrypt_password(self):
            self.__failed_attempts = 0
            return "인증 성공"
        else:
            self.__failed_attempts += 1
            return f"인증 실패 {self.__failed_attempts}/3"


secutiry = SecuritySystem("secret123")
print(secutiry.authenticate("wrong"))
print(secutiry.authenticate("secret123"))
'''


'''
class Circle1:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14*self.radius ** 2

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, radius):
        self.radius = radius


c1 = Circle1(5)
print(c1.get_area())   # 메서드 호출 : 괄호 필요
c1.set_radius(10)
print(c1.get_area())


c2 = Circle2(4)
print(c2.area)   # 속성 접근 : 괄호 없이 사용 가능
c2.radius = 10
print(c2.area)
'''


# 실습3
# 문제1
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            print("비밀번호 변경")
            self.__password = new_pw

        else:
            print("비밀번호 불일치")

    def check_password(self, password):
        if self.__password == password:
            print("비밀번호 일치")
        else:
            print("비밀번호 불일치")


user = UserAccount("정은경", "wjddmsrud")

user.check_password("wjddmsrud")

user.change_password("wjddmsrud", "dmsruddl")


# 문제2
class Student:
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("점수는 0 이상 100이하만 허용됩니다.")


s1 = Student(80)
s1.score = 90
print(s1.score)
