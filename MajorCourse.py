from Course import Course

class MajorCourse(Course):
    def __init__(self, courseName: str, credit: int, isRequired: str):
        super().__init__(courseName, credit)
        self.isRequired = isRequired

    def set_prerequisite(self,precourse: str) -> str:
        return f"'{self.courseName}' 강의({self.credit}학점,{self.isRequired})는 '{precourse}' 과목을 선수강과목으로 수강하여야 합니다."