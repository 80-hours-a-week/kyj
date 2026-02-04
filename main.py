#!/usr/bin/env python3

from person import Person
from professor import Professor
from student import Student
from graduate_student import GraduateStudent
from undergraduate_student import UndergraduateStudent
from course import Course
from major_course import MajorCourse
from liberal_art_course import LiberalArtCourse
from log_generator import log_stream
from presenters import (
    render_teach_event,
    render_thesis_event,
    render_internship_event,
    render_prerequisite_event,
    render_course_run_event,
)
from enums import (
    ProgramType,
    EnrollmentStatus,
    MajorRequirement,
    LiberalArtCategory,
    DeliveryMode,
)


def _parse_enum(value: str, enum_cls: type, label: str):
    """입력 문자열을 Enum으로 변환. 허용되지 않은 값이면 ValueError."""
    value = value.strip()
    for member in enum_cls:
        if member.value == value:
            return member
    allowed = ", ".join(m.value for m in enum_cls)
    raise ValueError(f"{label}: '{value}'는 허용되지 않습니다. ({allowed})")


def _parse_internship(value: str) -> str:
    """현장실습 참여 여부: '참여' 또는 '불참여'만 허용."""
    value = value.strip()
    if value in ("참여", "불참여"):
        return value
    raise ValueError(f"현장실습 참여 여부: '{value}'는 허용되지 않습니다. (참여, 불참여)")


def main():
    events: list[str] = []
    students: list[Student] = []
    courses: list[Course] = []

    try:
        # Professor 입력
        pname = input("교수 이름: ")
        page = int(input("교수 나이: "))
        dept = input("교수 학과: ")
        professor = Professor(pname, page, dept)
        professor.perform_teaching()
        events.append(render_teach_event(professor))
        print(render_teach_event(professor) + '\n')

        # GraduateStudent 입력
        gsname = input("대학원생 이름: ")
        gsage = int(input("대학원생 나이: "))
        gsmajor = input("대학원생 전공: ")
        ptype = _parse_enum(input("대학원 과정(석사/박사): "), ProgramType, "대학원 과정")
        gradsd = GraduateStudent(gsname, gsage, gsmajor, ptype)
        students.append(gradsd)
        gradsd.start_thesis()
        events.append(render_thesis_event(gradsd))
        print(render_thesis_event(gradsd) + '\n')

        # UndergraduateStudent 입력
        ugsname = input("대학생 이름: ")
        ugsage = int(input("대학생 나이: "))
        ugsmajor = input("대학생 전공: ")
        en_st = _parse_enum(input("현재 구분(재학/휴학/졸업): "), EnrollmentStatus, "현재 구분")
        ugradsd = UndergraduateStudent(ugsname, ugsage, ugsmajor, en_st)
        students.append(ugradsd)
        p = _parse_internship(input("현장실습 참여 여부(참여/불참여): "))
        ugradsd.participate_internship(p)
        events.append(render_internship_event(ugradsd))
        print(render_internship_event(ugradsd) + '\n')

        # MajorCourse 입력
        mname = input("전공 강의명: ")
        mcredit = int(input("전공 학점: "))
        is_req = _parse_enum(input("전공핵심/전공선택: "), MajorRequirement, "전공 구분")
        mcourse = MajorCourse(mname, mcredit, is_req)
        courses.append(mcourse)
        pre = input("선수강과목: ")
        mcourse.set_prerequisite(pre)
        events.append(render_prerequisite_event(mcourse))
        print(render_prerequisite_event(mcourse) + '\n')

        # LiberalArtCourse 입력
        lname = input("교양 강의명: ")
        lcredit = int(input("교양 학점: "))
        cat = _parse_enum(input("교양 구분(인문/사회/자연/예체능): "), LiberalArtCategory, "교양 구분")
        lcourse = LiberalArtCourse(lname, lcredit, cat)
        courses.append(lcourse)
        onoff = _parse_enum(input("온/오프라인(온라인/오프라인): "), DeliveryMode, "진행 방식")
        lcourse.run(onoff)
        events.append(render_course_run_event(lcourse))
        print(render_course_run_event(lcourse) + '\n')

        # 다형성 활용: 구체 타입 없이 공통 메서드로 처리
        print("[학생 활동 요약]")
        for student in students:
            print(f"  - {student.describe_activity()}")
        print("[강의 목록]")
        for course in courses:
            print(f"  - {course.describe()}")
        print("[강의 운영 방식 요약]")
        for course in courses:
            print(f"  - {course.describe_operation()}")

    except ValueError as e:
        print("[입력 오류]", e)
        return

    # 제네레이터로 순차 로그 출력
    for log in log_stream(events):
        print(log)

main()