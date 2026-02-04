from typing import Optional

from student import Student
from enums import EnrollmentStatus, InternshipParticipation


class UndergraduateStudent(Student):
    def __init__(self, name: str, age: int, major: str, enrollment_status: EnrollmentStatus):
        super().__init__(name, age, major)
        self.enrollment_status = enrollment_status
        self.internship_participation: Optional[InternshipParticipation] = None

    def describe_activity(self) -> str:
        return "현장실습에 참여합니다."

    def participate_internship(self, participate: InternshipParticipation) -> None:
        """현장실습 참여(도메인 행위). 상태만 변경하고 출력은 하지 않음."""
        self.internship_participation = participate
