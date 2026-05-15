# main,person(자식),actor/programmer.py

from person import Person


class Programmer(Person):  # ()안에 부모
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer")
        # super()는 부모(person)를 뜻함, 부모의 셍성자 호출해서 이름,나이 저장 기능재사용
        self.language = language  # 개발자에게만 방을 하나 더만듬

    def introduce(self):
        super()._hello()  # 부모의 hello가져와 먼저 실행
        # 나이는 지금 출력안됨 코드안써서.
        print(
            f"나는 {self.language}언어로 프로그래밍 할수 있습니다"
        )  # 자기만의 추가 대시 출력
