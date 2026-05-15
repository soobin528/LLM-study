# import calc.basic, calc.advanced

# 패키지 안에있는 모듈 하나하나를 가져오는게 아니라 패키지를 가져왔을떄 모듈이 자동으로 가져오는 형태로 구성
# --> 패키지의 __init__.py
import calc  # 자동으로 init파이썬 파일이 실행되고 init에 있는 두개의 모듈이 임포트됨

print(calc.basic.add(3, 7))
print(calc.advanced.div(3, 7))
