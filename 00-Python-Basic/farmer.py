from person import Person


class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job="Farmer")
        self.fruit = fruit

    def introduce(self):
        super()._hello()
        print(f"저는 {self.fruit}을 기릅니다")

# person은 추상클래스가 되고 introduce는 추상 메소드가 되어 실제로 person클래스 자체는 이 내용 구현안해도됨
# 그러나 person을 상속받는 프로그래머, 액터 클래스들은 모두 introduce메소드를 구현해야함 
# 이 구현해야햐는 부분이 def introduce 부분? 자식 클래서으에서 이거 구현 안하면 안됨