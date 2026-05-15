# main(합쳐진 결과),person,actor/programmer/Farmer.py

from programmer import Programmer
from actor import Actor
from farmer import Farmer

""" 1.
# dave라는 개발자 생성
dave = Programmer("dave", 42, "python")
dave.introduce()

# 출력 : hello im dave
# 나는 파이썬 언어로 프로그래밍할수있습니다

song = Actor("song", 55, "parasite")
song.introduce()


kim =Actor("song", 55, "parasite")
song.introduce()
"""

""" 2. 
# 세 자식 클래스를 각각의 변수가 아닌 people이라고 하는 리스트에 넣어준다
people = [Programmer("dave", 42, "python"),
          Actor("song", 55, "parasite"),
          Actor("song", 55, "parasite")]

for person in people:
    person.introduce()
"""


# 3. 캡슐화
from programmer import Programmer

dave = Programmer("dave", 42, "python")
dave.__age = -1  # 이렇게 강제로 설정하였다면 기존의 Private 멤버변수로 제어가됨

dave._hello()  # dave.ge = -1이렇게되면 -1살이라고 출력이됨
