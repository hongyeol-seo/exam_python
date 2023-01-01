class Student:
    school = "대구중학교"
    # name = "서홍열"

    # 인스턴스 객체 생성 및 초기화 메서드
    def __init__(self, name, number, grade):
        self.name = name
        self.number = number
        self.grade = grade

    # 객체 미생성으로 사용 가능하는 메서드들
    @staticmethod
    def showSchoolname(count):
        Student.school = "Happy 중학교"  # 바로 바꿀 수가 있다.
        print(f'{Student.school}-{count}')

    @classmethod  # 클래스 정보를 넘겨준다. / 현재 이메서드를 가지고 있는 객체의 주소값을 전달해준다.
    def printSchool(cls, count):
        # print(f'{cls.name}')
        print(f'{cls.school}-{count}')

    #test 클래스메서드
    # @classmethod
    def t_printschool(cls,count):
        print(f'{cls.school} - {count}')

# 클래스 및 객체 사용하기
print(Student)
print(Student.school)
Student.showSchoolname(1)
Student.printSchool(2)


# ------------------------------------------------
# 대학생 정보를 담고 있는 클래스
# 클래스명 BigStudent
# 속성 : 학교, 학과, 번호, 학년, 전공
# ------------------------------------------------

class BingStudent(Student):
    # 클래스 변수
    school = "한국대학교"

    # 인스턴스 즉, 객체 생성 및 속성 초기화 메서드
    def __init__(self, name, number, grade, major):
        super().__init__(name, number, grade)
        self.major = major

BingStudent.showSchoolname(2) #정적메서드
BingStudent.printSchool(2) #클래스메서드 

