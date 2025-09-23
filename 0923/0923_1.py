# 상속
'''
기존 클래스의 속성과 메서드를 쿨려받아 새로운 클래스를 만드는 것

동물 : 포유류 -> 개, 고양이
자동차 : 차량 -> 승용차, 트럭
가족 : 부모 -> 자식
'''


# 기본 문법과 용어
'''
class 부모클래스:
    pass


class 자식클래스(부모클래스):
    pass
'''
# 자식은 부모의 모든 것을 물려 받는다
# 부모의 모든 속성과 메서드를 자동으로 사용 가능
# 추가된 자신만의 속성과 메서드 정의 가능


from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"안녕하세요. {self.name}입니다.")


class Student(Person):
    def study(self):
        print(f"{self.name}이(가) 공부합니다.")


class Teacher(Person):
    def teach(self):
        print(f"{self.name}이(가) 수업합니다.")


student = Student("김학생", 20)
teacher = Teacher("박선생", 35)


# 부모 클래스 메서드 호출
student.greet()
teacher.greet()

# 자식 클래스 메서드 호출
student.study()
teacher.teach()


# super()와 생성자 상속
# super()는 자식 클래스에서 부모 클래스에 접근할 때 사용

# super() 없이 - 문제 발생
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(F"Person 생성 : {name} {age}살")

    def greet(self):
        print(f"안녕하세요. {self.name}입니다.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print(f"Student 생성 : 학번 {student_id}")

    def greet(self):
        super().greet()
        print("학생입니다.")


student = Student("김철수", 20, "20250001")
print(student.name)
student.greet()


# 메서드 오버라이딩
# 오버라이딩
# 부모 클래스의 메서드를 자식 클래스에서 다시 정의하는 것

class Animal:
    def make_sound(self):
        print(f"동물이 소리를 냅니다.")


class Dog(Animal):
    def make_sound(self):
        print("멍멍")


class Cat(Animal):
    def make_sound(self):
        print("야옹")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}의 넓이 : {self.area()}")


class Ractangle(Shape):
    def __init__(self, width, height):
        super().__init__("직사각형")
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("원")
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


shapes = [Ractangle(5, 3), Circle(4)]
for shape in shapes:
    shape.info()


# 실습4
# 문제1
class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printinfo(self):
        print(f"변의 개수 : {self.sides}")
        print(f"밑변의 길이 : {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")


class Ractangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f"넓이 : {self.base*self.height}")


class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(f"넓이 : {(self.base*self.height)/2}")


shapes = [Ractangle(4, 10, 5), Triangle(3, 10, 2)]
for shape in shapes:
    shape.printinfo()
    shape.area()


# 추상 클래스
'''
직접 객체를 만들 수 없고, 반드시 상속 받아서 완성해야 사용할 수 있는 미완성 설계도

동물 - 실제로 "동물"만 있는 건 없고, 개, 고양이, 새, 등 구체적인 동물이 있음
악기 - 추상적 개념, 피아노, 기타, 드럼이 구체적 개념
'''


# 추상 클래스 없이
class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def eat(self):
        print("강아지가 밥을 먹습니다.")


dog = Dog()
dog.make_sound()


'''
# 추상클래스 사용
class Animal(ABC):  # 추상 클래스
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def eat(self):
        print("강아지가 밥을 먹습니다.")
'''


# 기본 사용법
# for abc import ABC, abstractmethod

class 추상클래스이름(ABC):   # ABC 상속 필수 !
    @abstractmethod
    def 추상메서드(self):
        pass


# 추상 메서드는 자식 클래스에서 반드시 구현


class Animal(ABC):   # 추상 클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 일반 메서드 - 모든 동물이 공통으로 사용

    def sleep(self):
        print(f"{self.name}이(가) 잠을 잡니다.")

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")

    # 추상 메서드 - 각 동물마다 다르게 구현해야 함

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: 멍멍!")

    def move(self):
        print(f"{self.name}이(가) 뛰어다닙니다.")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name}: 짹짹")

    def move(self):
        print(f"{self.name}이(가) 날아갑니다.")


dog = Dog("바둑이", 3)
bird = Bird("참새", 1)


# 부모 클래스의 일반 메서드
dog.eat()
bird.sleep()


# 부모 클래스의 추상 메서드
dog.move()
bird.make_sound()


# from abc import ABC, abstractmethod
# 실습5
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")


card = CardPayment()
cash = CashPayment()

card.pay(5000)
cash.pay(10000)
