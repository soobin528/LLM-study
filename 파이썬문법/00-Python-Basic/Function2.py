# 기본 매개 변수 : 함수 정의에서 매개 변수에 기본값을 할당하는 것.
# 기본 매개 변수를 사용하면 함수 호출 시 해당 매개 변수에 값을 제공하지 않아도 됨. 기본값이 사용
# 기본 매개 변수는 일반 매개 변수 뒤에 위치해야 합니다. 그렇지 않으면 구문 오류가 발생
# 일반 매개 변수 : 함수 호출 시 반드시 값을 제공
# 기본 매개 변수 : 함수 호출 시 값을 제공하지 않아도 됨


def welcome(
    city, name="Guest", room=None
):  # 일반 매개변수(city) 뒤에 기본매개변수 위치(name)
    if room is None:
        room = (
            []
        )  # 기본값이 변경 가능한 객체인 경우, 함수가 호출될 때마다 새로운 객체를 생성하도록 None을 사용하여 처리

    print(f"Hello, {name}! Welcome to {city}, and your room is {room}")


welcome("New York")  # Hello, Guest! Welcome to New York, and your room is []
welcome("Los Angeles", "Bob")  # Hello, Bob! Welcome to Los Angeles, and your room is []
welcome(
    "Chicago", "Alice", [101, 102]
)  # Hello, Alice! Welcome to Chicago, and your room is [101, 102]


# 키워드 인자 : 함수 호출 시 매개 변수의 이름을 명시하여 값을 전달.
# 매개 변수의 순서에 상관없이 값을 전달 가능.
# 일반 매개 변수와 기본 매개 변수 모두에 사용가능


def display_info(name, age, city):
    print(f"Name : {name}, Age: {age}, City: {city}")


display_info(
    name="Alice", age=30, city="New York"
)  # Name : Alice, Age: 30, City: New York
display_info(city="Los Angeles", name="Bob", age=25)  # Name : Bob


# 가변 인자 리스트 : 함수가 호출될 때 전달되는 인자의 개수가 고정되어 있지 않을 때 사용
# *args : 위치 인자들을 튜플로 전달
# 가변 인자 리스트는 일반 매개 변수와 기본 매개 변수 뒤에 위치해야 한다
def calc_sum(*args):
    total = 0
    for org in args:
        total += org  # total = total + org
    return total


print(calc_sum(1, 2, 3))  # 6
print(calc_sum(4, 5))  # 9
print(calc_sum())  # 0


# 키워드 가변인자 리스트
# 키워드 인자들을 딕셔너리로 전달
# 일반 매개 변수와 기본 매개 변수 뒤에 위치해야 한다
# 함수 정의에서 **kwargs를 사용하여 키워드 가변 인자 리스트를 처리
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"P{key}:{value}")


print_info(name="EVE", age=28, city="Berelin")
