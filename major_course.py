from course import Course
from enums import MajorRequirement


class MajorCourse(Course):
    def __init__(self, courseName: str, credit: int, is_required: MajorRequirement):
        super().__init__(courseName, credit)
        self.is_required = is_required
        self.prerequisite = ""

    def describe(self) -> str:
        return f"'{self.courseName}' 전공 강의 ({self.credit}학점)"

    def describe_operation(self) -> str:
        return "선수강과목을 지정합니다."

    def set_prerequisite(self, precourse: str) -> None:
        """선수강과목 지정(도메인 행위). 상태만 변경하고 출력은 하지 않음."""
        self.prerequisite = precourse
