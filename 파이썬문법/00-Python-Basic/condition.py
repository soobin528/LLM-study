 # 단일 조건 조건문
value = 30

# 이 값이 20을 초과하는 경우 Big! 이라는 메시지를 출력
if value > 20:
    print("Big!")   # 조건이 참인 경우 실행되는 코드 블록

# 20보다 큰 경우는 Big, 그렇지 않은 경우 small
if value > 20:
    print("Big!")
else:    
    print("Small!")

#50보다 큰경우 great, 20보다 큰 경우 big, 그렇지 않은 경우 small
if value > 50:
    print("Great!")
elif value > 20:
    print("Big!")
else:    
    print("Small!")


# 날씨가 흐리고 강수확률이 70% 이상이면 -> 비가온다 우산을 챙겨라

condition = "맑음"
rain_rate = 0.70

if condition is "흐림" and rain_rate >= 0.70:
    print("비가 온다. 우산을 챙겨라.")
elif condition is "흐림" and rain_rate < 0.70:
    print("비가 올 수도 있다. 우산을 챙겨라.")
else:
    print("비가 오지 않는다. 우산은 필요 없다.")


#사용자로부터 두 개의 값을 입력받는디
#입력값을 숫자로 변환
# 첫번째 값이 크다면 Win, 두번째 값이 크다면 Lose, 같다면 Draw를 출력한다

value1 = int(input("첫 번째 값을 입력하세요: "))
value2 = int(input("두 번째 값을 입력하세요: "))

# 입력값을 숫자로 변환
#num_value1= int(value1)
#num_value2= int(value2)

if value1 > value2:
    print("Win")
elif value1 < value2:
    print("Lose")
else:
    print("Draw")



# 시험점수를 입력받는다.
# 점수가 비정상 범위면 아무것도 실행되지앟는다
# 점수의 각 등급에 따른 결과를 출력한다

#score=int(input("시험 점수를 입력하세요: "))
score_str= input("시험 점수를 입력하세요: ")

score=int(score_str)

if score > 99 or score <1:
    print("점수가 비정상 범위입니다.")
elif score >=90:
    print("A")
elif score >=80:
    print("B")                  
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")



# 
if score <= 99 and score >= 90:
    grade = "A"
elif score <=89 and score >= 80:
    grade = "B"
elif score <=79 and score >= 70:
    grade = "C"
elif score <=69 and score >= 60:
    grade = "D"
elif score <=59 and score >= 1:
    grade = "F"
else:
    grade = "None"

if grade is not None:
    print(f"점수는 {score}이고, 등급은 {grade}입니다.")
