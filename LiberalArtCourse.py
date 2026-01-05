from Course import Course

class LiberalArtCourse(Course):
    def __init__(self, courseName: str, credit: int, category: str):
        super().__init__(courseName, credit)
        self.category = category

    def run(self, isonline: str) -> str:
        return f"[구분: {self.category}] '{self.courseName}' 강의({self.credit}학점)는 {isonline}으로 진행됩니다."
