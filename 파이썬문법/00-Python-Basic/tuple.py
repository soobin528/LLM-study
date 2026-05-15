# 빈 튜플 생성
my_tuple = (1,) # 요소가 하나인 튜플을 만들 때는 쉼표를 꼭 붙여야 함

# 과일 바구니
fruit = ("apple", "banana", "cherry")
first=fruit[0]
print(first) # apple 

# 패킹과 언패킹
# 패킹: 여러 값을 하나의 튜플로 묶는 것
tp = 1,2,3
print(tp) #(1,2,3)

# 언패킹: 튜플의 요소를 개별 변수에 할당하는 것
v1,v2,v3 = tp
print(f"{v1}, {v2}, {v3}") # 1,2,3


# 패킹을 사용하면 이렇게 복잡하게 하지않아도됨
a = 10
b = 20
print(f"Before swapping: a={a}, b={b}") # Before swapping: a=10, b=20

temp = a # a=10, b=20, temp=10
a = b # a=20, b=20, temp=10
b = temp # a=20, b=10, temp=10
print(f"After swapping: a={a}, b={b}") # After swapping: a=20, b=10 

a,b = b,a #(20,10) -> a=20, b=10 #이렇게 간단하게 할 수 있음
#print("a:" ,a) # a: 20
#print("b:" ,b) # b: 10

tp1=(1,2,3,4,5,6,7,8,9,10)
val1, val2, val3, *vals =tp1
print(val1) # 1
print(val2) # 2
print(val3) # 3
print(vals) # [4,5,6,7,8,9,10]  # *를 사용하면 나머지 요소들을 리스트로 받을 수 있음

vals.append(11) # 리스트이기 때문에 append 가능
print(vals) # [4,5,6,7,8,9,10,11]   