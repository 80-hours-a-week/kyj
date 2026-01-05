from Person import Person

class Student(Person):
    def __init__(self, name: str, age: int, major: str):
        super().__init__(name, age)
        self.major = major

    def enrollCourse(self, course_name: str) -> str:
        return f"{self.name}({self.major},{self.age}세) 학생이 '{course_name}' 수업을 등록하였습니다."