"""도메인 상태값을 표현하는 Enum 및 Literal 타입 정의."""

from enum import Enum
from typing import Literal


# 대학원 과정
class ProgramType(Enum):
    MASTER = "석사"
    DOCTOR = "박사"


# 재학/휴학/졸업
class EnrollmentStatus(Enum):
    ENROLLED = "재학"
    LEAVE = "휴학"
    GRADUATED = "졸업"


# 현장실습 참여 여부 (Literal로 최소 제약)
InternshipParticipation = Literal["참여", "불참여"]


# 전공 강의 구분
class MajorRequirement(Enum):
    CORE = "전공핵심"
    ELECTIVE = "전공선택"


# 교양 구분
class LiberalArtCategory(Enum):
    HUMANITIES = "인문"
    SOCIAL = "사회"
    SCIENCE = "자연"
    ARTS = "예체능"


# 강의 진행 방식 (온/오프라인)
class DeliveryMode(Enum):
    ONLINE = "온라인"
    OFFLINE = "오프라인"
