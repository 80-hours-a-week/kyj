from person import Person


class Professor(Person):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department
        self.has_taught = False

    def perform_teaching(self) -> None:
        """강의 수행(도메인 행위). 상태만 변경하고 출력은 하지 않음."""
        self.has_taught = True

