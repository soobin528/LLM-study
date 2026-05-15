# for loop
for i in range(1,5): #1,2,3,4
    print(i) 
else:
    print("반복이 완료되었습니다.")


# while loop
i=0
while i<5:
    print(i)
    i+=1
else:
    print("while 반복이 완료되었습니다.")


fruits = ['사과', '딸기', '복숭아', '포도']

for fruit in fruits:
    if fruit == '사과':
        print("사과는 맛있습니다.")
    print(f"{fruit}이(가) 과일바구이네 있습니다.")



while True:
    user_input=input("명령어를 입력해주세요: ")
    if user_input =="종료":
        pass
    else:
        pass   #TODO : 차후 개발 예정


#구구단 프로그램
#1단 - 9단, n * 1 ~ n * 9
for x in range(1,10):
    for y in range(1,10):
        print(f"{x} * {y} = {x*y}" )



#enumerate 활용하기
fruits = ["사과", "딸기", "복숭아", "포도"]

index=1
for fruit in fruits:
    print(f"{index}번쨰 과일은 {fruit}입니다.") 


for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번쨰 과일은 {fruit}입니다.")


# 팩토리얼 구하기
# n * (n-1) #...*2*1
#5! = 5 * 4 * 3 * 2 * 1

num=10
result=1

for i in range(1,num+1):
    result = result * i

print(f"{num}!은 {result}입니다.")
