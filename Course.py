from abc import ABC, abstractmethod


class Course(ABC):
    """모든 강의가 공통으로 가져야 하는 행위의 기준점."""

    def __init__(self, courseName: str, credit: int) -> None:
        self.courseName = courseName
        self.credit = credit

    def summary(self) -> str:
        """강의명과 학점에 대한 공통 요약. 모든 하위 클래스에서 동일하게 사용."""
        return f"{self.courseName} ({self.credit}학점)"

    @abstractmethod
    def describe(self) -> str:
        """강의 유형(전공/교양 등)을 포함한 설명. 하위 클래스에서 구현해야 합니다."""
        raise NotImplementedError

    @abstractmethod
    def describe_operation(self) -> str:
        """강의 유형별 운영 방식을 반환합니다. 하위 클래스에서 구현해야 합니다."""
        raise NotImplementedError

