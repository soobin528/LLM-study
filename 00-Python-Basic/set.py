empty_set = set() #{}는 딕셔너리를 만들 때 사용하는 기호이므로 빈 집합을 만들 때는 set() 함수를 사용해야 함
my_set = {1, 2, 3, 3}
print(empty_set) # set() # 빈 집합은 이렇게 만들어야 함
print(my_set) # {1, 2, 3} # 중복된 요소는 하나만 저장됨

#1.
fruits = {"apple", "banana", "cherry"}
print(fruits) 
# {'banana', 'cherry', 'apple'} # 집합은 순서가 없기 때문에 요소의 순서가 바뀔 수 있음 -> 대괄호 통해서 인덱싱 불가

#2. 요소 추가 및 제거
fruits.add("orange") # 요소 추가
print(fruits) # {'banana', 'cherry', 'apple', 'orange'} 

fruits.remove("banana") # 요소 제거
print(fruits) # {'cherry', 'apple', 'orange'}

#3. 집합 연산
fruits1={"apple", "strawberry", "peach"}
fruits2={"banana", "strawberry", "apple"}

# 합집합
union_set = fruits1 | fruits2
print(union_set) # {'banana', 'strawberry', 'peach', 'apple'} # 중복된 요소는 하나만 저장됨

# 교집합
intersection_set = fruits1 & fruits2
print(intersection_set) # {'strawberry', 'apple'}

# 차집합 (순서 중요)
difference_set = fruits1 - fruits2
print(difference_set) # {'peach'} # fruits1에는 있지만 fruits2에는 없는 요소

# 대칭차집합
symmetric_difference_set = fruits1 ^ fruits2
print(symmetric_difference_set) # {'banana', 'peach'} # fruits1과 fruits2 중에서 한 집합에만 있는 요소 

#issubset() : 부분집합인지 확인
print(fruits1.issubset(union_set)) # True # fruits1은 union_set의 부분집합인가? 
print(fruits2.issubset(union_set)) # True # fruits2는 union_set의 부분집합인가?