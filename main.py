#!/usr/bin/env python3

from Person import Person
from Professor import Professor
from Student import Student
from graduate_student import graduate_student
from undergraduate_student import undergraduate_student
from Course import Course
from MajorCourse import MajorCourse
from LiberalArtCourse import LiberalArtCourse
from log_generator import log_stream

def main():
    events: list[str] = []

    try:
        # Professor 입력
        pname = input("교수 이름: ")
        page = int(input("교수 나이: "))
        dept = input("교수 학과: ")
        professor = Professor(pname, page, dept)
        events.append(professor.teach())
        print(professor.teach()+'\n')

        # graduate_student 입력
        gsname = input("대학원생 이름: ")
        gsage = int(input("대학원생 나이: "))
        gsmajor = input("대학원생 전공: ")
        ptype = input("대학원 과정: ")
        gradsd = graduate_student(gsname,gsage,gsmajor,ptype)
        events.append(gradsd.write_thesis())
        print(gradsd.write_thesis()+'\n')

        # undergraduate_student 입력
        ugsname = input("대학생 이름: ")
        ugsage = int(input("대학생 나이: "))
        ugsmajor = input("대학생 전공: ")
        en_st = input("현재 구분(재학/휴학/졸업): ")
        ugradsd = undergraduate_student(ugsname,ugsage,ugsmajor,en_st)
        p = input("현장실습 참여 여부(참여/불참여): ")
        events.append(ugradsd.internship(p))
        print(ugradsd.internship(p)+'\n')

        # MajorCourse 입력
        mname = input("전공 강의명: ")
        mcredit = int(input("전공 학점: "))
        isReq = input("전공핵심/전공선택: ")
        mcourse = MajorCourse(mname, mcredit, isReq)
        pre = input("선수강과목: ")
        events.append(mcourse.set_prerequisite(pre))
        print(mcourse.set_prerequisite(pre)+'\n')

        # LiberalArtCourse 입력
        lname = input("교양 강의명: ")
        lcredit = int(input("교양 학점: "))
        cat = input("교양 구분: ")
        lcourse = LiberalArtCourse(lname, lcredit, cat)
        onoff = input("온/오프라인: ")
        events.append(lcourse.run(onoff))
        print(lcourse.run(onoff)+'\n')


    except ValueError as e:
        print("[입력 오류]", e)
        return 

    # 제네레이터로 순차 로그 출력
    for log in log_stream(events):
        print(log)

main()