from abc import ABC, abstractmethod
from person import Person


class Student(Person, ABC):
    def __init__(self, name: str, age: int, major: str):
        super().__init__(name, age)
        self.major = major

    @abstractmethod
    def describe_activity(self) -> str:
        """학생 유형별 주요 활동을 반환합니다. 하위 클래스에서 구현해야 합니다."""
        raise NotImplementedError

    def enrollCourse(self, course_name: str) -> str:
        return f"{self.name}({self.major},{self.age}세) 학생이 '{course_name}' 수업을 등록하였습니다."
