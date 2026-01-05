from Person import Person

class Professor(Person):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name,age)
        self.department = department

    def teach(self) -> str:
        return f"{self.name} 교수({self.age}세)는 {self.department} 학생들을 가르칩니다."
    

