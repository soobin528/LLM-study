def func():
    print("This is a function")


func()  # 함수 호출


def sum(num1, num2):
    return num1 + num2


def div(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2  # 함수는 반환을 하는순간 함수는 종료


result = sum(10, 20)
print(result)  # 30

result = div(10, 0)
print(result)  # 0
