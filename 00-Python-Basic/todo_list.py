#todo_list를 어떻게 저장할 것인가?
# 리스트로 저장할 수 있다. 리스트는 순서가 있고, 변경 가능하다.
# 할일을 추가/삭제해야하는 가변 데이터 접근 -> 튜플은 안됨
# 할일의 속성들이 포함되어야한다면 -> 딕셔너리가 더 적합
# 할일은 입력된 순서가 중요하다면 -> 리스트

# 할 일 목록을 리스트로 저장

todo_list = []

while True:
    print("")
    print("할 일 목록 관리자")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 종료")

    choice = input("원하는 작업을 선택하세요 (1-4): ")
    
    if choice == "1":
        todo = input("추가할 일:")
        todo_list.append(todo)
        print(f"{todo} 할 일이 추가 되었습니다")

    elif choice == "2":
        todo = input("삭제할 일:")
        todo_list.remove(todo)
        print(f"{todo} 할 일이 삭제 되었습니다")

        
    elif choice == "3":
        print(todo_list)
    elif choice == "4":
        break
    else:
        print("올바른 선택이 아닙니다. 다시 시도하세요.")
        