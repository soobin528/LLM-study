while True:

    try:
        num1 = int(input("첫번쨰 숫자를 입력해주세요"))
        num2 = int(input("두번쨰 숫자를 입력해주세요"))
        result = num1 / num2
        print(f"나누기 결과는 {result}입니다.")
        break
    except ValueError:
        print(f"정상적인 숫자를 입력해주세요")
        continue
    except ZeroDivisionError:
        print(f"0으로 나눌 수 없습니다. 다시 입력해주세요.")
        continue
    except:
        pass 