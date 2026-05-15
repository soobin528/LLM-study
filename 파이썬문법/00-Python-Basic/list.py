my_list=[10,20,30]
my_list.append(10)
my_list.append(15)
my_list.append(20)
print(my_list)
print(len(my_list))

element=my_list[4]
print(element)

sliced = my_list[3:]
print("sliced:",sliced)

fruits=["banana","apple","blueberry","cherry"]

#바나나가 포함되어있나요?
is_banana_included ="banana" in fruits
print("Is banana included?", is_banana_included)


#체리는 어디에 있나요?
index_cherry = fruits.index("cherry")
print("cherry is", index_cherry)

#리스트의 정렬
numbers= [4,2,1,3,8,6,9,7,5]
print("unsorted",numbers)

numbers.sort()
print("sorted",numbers)

numbers.sort(reverse=True)
print("sorted in reverse",numbers)

#리스트의 요소 추가 및 제거
my_list=[]
my_list.append(10)
my_list.append(11)
my_list.append(12)
print(my_list)
# [10,11,12]


#리스트 한번에
my_list.extend([20,30,40])

print(my_list)
# [][10,11,12,20,30,40]

my_list.append([50,60]) #리스트 자체가 요소로 추가됨
# [10,11,12,20,30,40,[50,60]]

print(my_list[-1])
# [50,60]

#리스트 연산(+,*)
new_list = my_list + [70,80]
print(new_list)
# [10,11,12,20,30,40,[50,60],70,80]

multi_list= my_list * 2
print(multi_list)
# [10,11,12,20,30,40,[50,60],10,11,12,20,30,40,[50,60]] #반복된 리스트가 만들어짐

print(my_list)
# [10,11,12,20,30,40,[50,60]] #원본 리스트는 변하지 않음

del my_list[2] #인덱스 2에 있는 요소 제거
print(my_list)
# [10,11,20,30,40,[50,60]]  

max_value=max(my_list)
min_value=min(my_list)
print(f"최대값은 {max_value}, 최소값은 {min_value}입니다.")
print(f"최대값과 최소값의 차이는 {max_value - min_value}입니다.")
