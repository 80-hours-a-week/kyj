from Student import Student

class graduate_student(Student):
    def __init__(self, name: str, age: int, major: str, programtype: str):
        super().__init__(name, age, major)
        self.programtype = programtype

    def write_thesis(self) -> str:
        return f"[{self.programtype} 과정] {self.name}({self.major},{self.age}) 학생이 논문을 작성합니다."
