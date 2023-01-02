# -----------------------------------------------------
# 데코레이터(Decorator) :
# - 메서드에 명확한 의미 부여
# - 형식 @XXXX
# -----------------------------------------------------
# 클래스 미 메서드 종류
# - 완성된 클래스
# - 미완성 클래스(추상 클래스)
# 메서드의 종류
# - 객체 생성해야만 사용할 수 있는 메서드 => self
#   인스턴스 메서드
# - 객체 생성없이 사용가능한  메서드 => cls
#    - 정적메서드 => 객체 없이 사용가능
#    - 클래스메서드 => 클래스 정보를(cls) 가진 객체 없이 사용 가능한 메서드
# -----------------------------------------------------
# 클래스 종류 
# 클래스 
# 미완성 클래스 

#           추상클래스(abstract class)
#           abc 모듈을 포함해서 사용
#           미구현(코드 없는 메서드) 메서드를 가지고 있는 클래스
#           오버라이딩 => 이름이랑 매개변수는 수정할 수 없지만, 구현부는 수정할 수 있다. => 상속이랑 관계있다.
# -----------------------------------------------------
# 학생 정보 클래스
# 클래스명 : Student
# 필드 : attribute
# 속성 :
#   클래스 속성 : school
#   인스턴스 속성 : name, number, grade
# 메서드 :
#   클래스 메서드 : 학교명 출력 가능
#   정적 메서드 : 학교명 출력 가능
# -----------------------------------------------------
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

# 클래스 및 객체 사용하기
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





















# # -----------------------------------------------------------------------------------------------------
# # 사용자 정의 클래스 / 커스텀 클래스
# # -----------------------------------------------------------------------------------------------------
# # 만들고자 하는 프로젝트에서 사용할 데이터를 저장하는 타입
# # -----------------------------------------------------------------------------------------------------
# # 학생 정보를 저장하고 출력
# # => 학교, 이름, 학년
# class A:
#     num=0

#     def __init__(self,num):
#         self.num=num
#         A.num=3

#     def d(self,m):
#         pass


#     def c(mkdfs):
#         pass


#     def b(num):
#         print(A.num)
#         A.c()
#         A.d(A)

#     # def b(self,num):
#     #     pass


# a=A(2)
# a.d(2)
# A.c()

# class A:
#     print('A')
#     pass
