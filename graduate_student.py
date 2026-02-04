from student import Student
from enums import ProgramType


class GraduateStudent(Student):
    def __init__(self, name: str, age: int, major: str, program_type: ProgramType):
        super().__init__(name, age, major)
        self.program_type = program_type
        self.is_writing_thesis = False

    def describe_activity(self) -> str:
        return "논문을 작성합니다."

    def start_thesis(self) -> None:
        """논문 작성 시작(도메인 행위). 상태만 변경하고 출력은 하지 않음."""
        self.is_writing_thesis = True
