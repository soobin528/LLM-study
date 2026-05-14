"""
class Person:

    def hello(self) : #메소드 정의할때 첫번째 파라미터는 무조건 self / 설명 : 객체가 할수있는 기능(메소드)정의
        print("Hello")

if __name__ == "__main__":
    man = Person()   #person가지고 man이라는 객체 생성, man은 person의 모든 기능 사용가능
    man.hello() # man에게 기능 실행
"""


class Person:
    # 객체 바깥에서 멤버변수를 사용하려고 선언하는 것이 아니라 클래스 정의 안에서 초기화된 값을 접근하여 사용
    # --> 초기값으로 활용할수있도록 생성자 이용

    # 객체마다 고유한 데이터(self.name을 가지고 이름을 던져줌)

    def __init__(
        self, name, age
    ):  # 생성자로 데이터 초기화 init: 객체가 태어날때 자동으로 가장 먼저실행되는 생성자
        self.name = (
            name  # 외부에서 받아옴 이름 데이터를 객체의 고유 저장공간인 self에 저장
        )
        self.name = age

    def hello(self):  # 생성자에 저장해둔 self.name
        print(f"Hello, I'm a {self.name}")

    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일수없습니다")
        else:
            self.age = age
            print("Now im a {slef.age}years")


if __name__ == "__main__":
    man = Person(
        "John", 30
    )  # 태어날때부터 이름을 john으로 지정해서 태어나게함, init함수의 name 파라미터로 전달
    man.hello()
    man.update_age(31)
