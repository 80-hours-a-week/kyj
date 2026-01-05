from Student import Student

class undergraduate_student(Student):
    def __init__(self, name: str, age: int, major: str, enrollment_status: str):
        super().__init__(name, age, major)
        self.enrollment_status = enrollment_status
    
    def internship(self, participate: str) -> str:
        return f"{self.name}({self.major},{self.age},{self.enrollment_status}중) 학생이 현장실습에 {participate}합니다."
