# main,person,actor/programmer.py

from  person import Person

class Actor(Person):
    def __init__(self,name,age,film):
        super().__init__(name,age,job="Actor")
        self.film=film
    
    def introduce(self):
        super()._hello()
        print(f"저희 데표작은 {self.film}입니다.")