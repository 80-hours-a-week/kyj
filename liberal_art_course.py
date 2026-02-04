from typing import Optional

from course import Course
from enums import DeliveryMode, LiberalArtCategory


class LiberalArtCourse(Course):
    def __init__(self, courseName: str, credit: int, category: LiberalArtCategory):
        super().__init__(courseName, credit)
        self.category = category
        self.delivery_mode: Optional[DeliveryMode] = None

    def describe(self) -> str:
        return f"'{self.courseName}' 교양 강의 ({self.credit}학점)"

    def describe_operation(self) -> str:
        return "온/오프라인으로 진행됩니다."

    def run(self, delivery_mode: DeliveryMode) -> None:
        """강의 진행 방식 설정(도메인 행위). 상태만 변경하고 출력은 하지 않음."""
        self.delivery_mode = delivery_mode
