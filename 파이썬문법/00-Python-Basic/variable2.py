# 문자열 변수 선언
str_var = "this is my python code."
#print(str_var)

num_var="12"
print(num_var.isdecimal()) #true
num1_var="12. "
print(num_var.isdecimal()) #False (띄어쓰기, 점)

#인덱싱 
print(str_var[11]) # p
print(str_var[-1]) #.
print(str_var[-5]) #c

#슬라이싱
print(str_var[11:17]) #python
print(str_var[11:-6]) #python


# 문자열의 더하기
inum1=12
inum2=34
print(inum1+inum2) #35

snum1="12"
snum2="34"
print(snum1+snum2) #1234
#print(sum * 3) #121212

#Format String
weather = "흐림"
temp = 15.8
# % code (%s, %d, %f)
res= " [%s / %f도]오늘날씨는 %s 입니다. 기온은 %f도 입니다." % (weather,temp,weather,temp)
print(res)

#.format()
res1 = "오늘 날씨는 {}입니다. 기온은 {}도 입니다".foramt(weather,temp)
print(res1)

# f"""
res2 = f"오늘 날씨는 {weather}입니다. 기온은 {temp}도 입니다"
print(res)

#사용자로부터 값을 입력받기 - 숫자를 입력해도 기본적으로 문자열로 나옴 숫자로 하고싶으면 정수형으로 변환
inp = input("값을 입력해주세요") #문자열

# 이값을 1더해서 출력하기
num=int(inp) + 1 #정수형
print(f"입력받은 값에 1을 더하면, {num}입니다.")