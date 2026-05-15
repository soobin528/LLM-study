my_dict={} #중괄호사용
my_dict["key"]="value" #딕셔너리에 요소 추가

print(my_dict) # {'key': 'value'}

person={"이름":"홍길동", "나이":30, "직업":"개발자"}
print(person) # {'이름': '홍길동', '나이': 30, '직업': '개발자'}

name= person["이름"]
print(name) # 홍길동

print(f"이름은 {person['이름']}, 나이는 {person['나이']},직업은 {person['직업']}입니다.") # 이름은 홍길동, 나이는 30,직업은 개발자입니다.

country = person["국적"] # 존재하지 않는 키에 접근하려고 하면 KeyError 발생
print(f"국적은 {country}입니다.") # KeyError: '국적'

#키가 존재하는지 확인하기 중요!!!
country = person.get("국적", "알 수 없음") # get() 메서드를 사용하면 키가 존재하지 않을 때 None 반환
print(f"국적은 {country}입니다.") # 국적은 알 수 없음입니다.

person["나이"] =31 # 나이 업데이트
print(person) # {'이름': '홍길동', '나이': 31, '직업': '개발자'}            

person["국적"]="대한민국" # 새로운 키-값 쌍 추가
print(person) # {'이름': '홍길동', '나이': 31, '직업': '개발자', '국적': '대한민국'}    



person_details = {"국적":"대한민국","결혼":True}
person.update(person_details) # 딕셔너리를 다른 딕셔너리로 업데이트

print(person) # {'이름': '홍길동', '나이': 31, '직업': '개발자', '국적': '대한민국', '결혼': True}