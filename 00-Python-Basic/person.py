"""
class Person:

    def hello(self) : #메소드 정의할때 첫번째 파라미터는 무조건 self / 설명 : 객체가 할수있는 기능(메소드)정의
        print("Hello")

if __name__ == "__main__":
    man = Person()   #person가지고 man이라는 객체 생성, man은 person의 모든 기능 사용가능
    man.hello() # man에게 기능 실행
"""

"""
# main,person(부모),actor/programmer.py 

class Person:
    # 객체 바깥에서 멤버변수를 사용하려고 선언하는 것이 아니라 클래스 정의 안에서 초기화된 값을 접근하여 사용
    # --> 초기값으로 활용할수있도록 생성자 이용

    # 객체마다 고유한 데이터(self.name을 가지고 이름을 던져줌)

    def __init__(
        self, name, age, job=None #일단 빈값으로 둠
    ):  # 생성자로 데이터 초기화 init: 객체가 태어날때 자동으로 가장 먼저실행되는 생성자
        self.name =  name  # 외부에서 받아옴 이름 데이터를 객체의 고유 저장공간인 self에 저
        self.age=age
        self.job = job

    def hello(self):  # 생성자에 저장해둔 self.name
        print(f"Hello, I'm  {self.name}")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일수없습니다")
        else:
            self.age = age
            print(f"Now im a {self.age}years")


if __name__ == "__main__":
    man = Person(
        "John", 30
    )  # 태어날때부터 이름을 john으로 지정해서 태어나게함, init함수의 name 파라미터로 전달
    man.hello()
    man.update_age(31)
"""


# person을 추상클래스로 만들기
from abc import ABC, abstractmethod


# 추상메소드 : 내용이 정의되지않은 메소드 이기 때문에 실제로 받아수 구현하는 구현체들에서 구현해야됨
class Person(ABC):

    def __init__(self, name, age, job=None):

        self.name = name
        self.__age = age  # __로 private 멤버 변수로 지정 가능 => 클래스 정의 안에서는 자유롭게 접근 가능하지만 ,, main.py에 접근할수없음?
        self.job = job

    # person은 추상클래스가 되고 introduce는 추상 메소드가 되어 실제로 person클래스 자체는 이 내용 구현안해도됨
    # 그러나 person을 상속받는 프로그래머, 액터 클래스들은 모두 introduce메소드를 구현해야함
    @abstractmethod
    def introduce(self):
        pass

    def _hello(self):  # _로 proteced 상속시 사용한 가능한메소드  
        print(f"Hello, I'm a {self.name}, {self.age} years old!")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일수없습니다")
        else:
            self.age = age
            print("Now im a {slef.age}years")
