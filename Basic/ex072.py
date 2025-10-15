class Student:
    count = 0 # self가 없으므로 class 변수 (Java : static 변수)

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print(f"{Student.count}번째 학생이 생성되었습니다.")

    @classmethod
    def print(cls):
        print("--클래스--메소드 호출")

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print(f"현재 생성된 총 학생 수는 {Student.count}명입니다.")
Student.print()
