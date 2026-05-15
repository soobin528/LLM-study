# 다이아모드 상속
class A:
    def method(self):
        print("im A")


class B(A):
    def method(self):
        print("im B")


class C(B):
    def method(self):
        print("im C")


class D(B, C):
    # 에러 : c는 이미 b를 상속받음 / 파이썬 원칙 : 자식을 부모보다 먼저 탐색(c,b)
    # 자식 클래스를 부모클래스보다 먼저적어야됨
    pass


d = D()
d.method()
print(D.mro())
# mro :메소드 탐색 순서
