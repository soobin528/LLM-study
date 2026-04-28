students = {} #딕셔너리 사용

# 입력대기창
while True:
    #메뉴 출력
    print("")
    print("1. 성적 입력하기")
    print("2. 학생 조회하기")
    print("3. 학점 조회하기")
    print("0. 종료하기")

    menu = input("메뉴를 번호를 입력하세요: ")
    
    #1. 성적 입력하기
    if menu == "1":
        #학생의 이름과 점수를 입력받아 저장
        name = input("학생의 이름을 입력해주세요.")
        score = input("학생의 점수를 입력해주세요.")

        #students[키] = 값
        students[name] = int(score) #학생의 이름을 key로, 점수를 value로 저장하기 (딕셔너리 활용)


        print(f"{name}의 성적은 {students[name]}점 입니다]")   #입력받은 학생의 이름과 점수를 출력하기
        

    #2. 학생 조회하기
    elif menu == "2":
        name = input("조회하고자 하는 학생의 이름을 입력하세요: ")
        if name in students.keys(): #학생의 이름이 딕셔너리에 존재하는지 확인하기
            print(f"{name}의 성적은 {students[name]} 점 입니다. ")
        else:
            print(f"{name}은 등록되지 않았습니다. 다시 입력해주세요.")


    #3. 학점 조회하기
    elif menu =="3":
        name = input("학점을 조회하고자 하는 학생의 이름을 입력하세요: ")
        if name not in students.key(): #학생의 이름이 딕셔너리에 존재하는지 확인하기
            print(f"{name}은 등록되지 않았습니다. 다시 입력해주세요.")
            continue   #학생의 이름이 딕셔너리에 존재하지 않을 경우 다시 메뉴 입력창으로 돌아가기 (while문 처음으로 돌아가기)
        score=students[name] #학생의 점수를 변수에 저장하기
        #A+ ~F 
        if score <= 90 and score >=90:
            grade = "A"
        elif score <= 89 and score >= 80:
            grade = "B"
        elif score <= 79 and score >= 70:
            grade = "C"
        elif score <= 69 and score >= 60:
            grade = "D"
        elif score <= 59 and score >= 1:
            grade = "F"
        else:
            grade='none'

        if grade in ['A', 'B', 'C', 'D']:
            mod = score % 10
            if mod >= 5:
                grade += "+"  
        
        print(f"{name}의 학점은 {grade}입니다.")


    #0. 종료하기
    elif menu =="0":
        break
    else:
        print("잘못된 메뉴입니다. 다시 입력해주세요.")
        continue   #잘못된 메뉴 입력시 다시 메뉴 입력창으로 돌아가기 (while문 처음으로 돌아가기)