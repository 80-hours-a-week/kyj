"""도메인 객체의 상태를 출력용 문자열로 변환하는 계층. 출력 형식 변경 시 이 모듈만 수정하면 됨."""

from graduate_student import GraduateStudent
from undergraduate_student import UndergraduateStudent
from major_course import MajorCourse
from liberal_art_course import LiberalArtCourse
from professor import Professor


def render_teach_event(professor: Professor) -> str:
    return f"{professor.name} 교수({professor.age}세)는 {professor.department} 학생들을 가르칩니다."


def render_thesis_event(student: GraduateStudent) -> str:
    return (
        f"[{student.program_type.value} 과정] "
        f"{student.name}({student.major},{student.age}세) 학생이 논문을 작성합니다."
    )


def render_internship_event(student: UndergraduateStudent) -> str:
    if student.internship_participation is None:
        raise ValueError("현장실습 참여 여부가 설정되지 않았습니다.")
    return (
        f"{student.name}({student.major},{student.age}세,{student.enrollment_status.value}중) "
        f"학생이 현장실습에 {student.internship_participation}합니다."
    )


def render_prerequisite_event(course: MajorCourse) -> str:
    return (
        f"'{course.courseName}' 강의({course.credit}학점,{course.is_required.value})는 "
        f"'{course.prerequisite}' 과목을 선수강과목으로 수강하여야 합니다."
    )


def render_course_run_event(course: LiberalArtCourse) -> str:
    if course.delivery_mode is None:
        raise ValueError("강의 진행 방식이 설정되지 않았습니다.")
    return (
        f"[구분: {course.category.value}] '{course.courseName}' 강의({course.credit}학점)는 "
        f"{course.delivery_mode.value}으로 진행됩니다."
    )
