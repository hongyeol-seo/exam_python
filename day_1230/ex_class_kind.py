# ----------------------------------------------------------------
# 사용자 정의 클래스 / 커스텀 클래스
# ----------------------------------------------------------------
# 만들고자 하는 프로젝트(프로그램)에서 사용할 데이터를 저장하는 타입
# ----------------------------------------------------------------
# 학생 정보를 저장하고 출력
# => 이름, 학교, 나이, 학년

# 변수이름 -> 리스트 -> 만약에 묶는다면?
class student:
    # 변수가 계속 추가된다?
    # school = []
    name = "홍열"
    # schoolName = 111 => 클래스에 변경/추가 한다면, 다 된다.

    #클래스 메서드! <=> 

    #새로운 메모리 공간에 할당
    #새로운 메모리 공간생성 => self에 담겨있다.
    def __init__(self,name,grande,school) -> None:
        self.name = name
        self.grade = grande
        self.school = school
        
    def study(suject) :
        print(f"{student.name}는{suject} 공부한다.")

    # FILE_NAME = "history.txt"
    
    # def __init__(self,file_name="history.txt"):
    #     self.FILE_NAME = file_name

    #     pass

    # 컴퓨터야 ! 클래스 안에 있는 변수의 이름을 찾아줘라!
    # self로 만들어서 사용하는 애들이 아니라, 클래스 변수라고 하는 애들은 클래스이름.속성
    # self가 있는 것들은 새로운 공간이 만들어진다. <=> 클래스 변수 . 모든 인스턴스가 공유한다.


s1 = student("길동","1학년","경북대")
s1.study()
student("단무지","2학년","대구대").study()


# 인스턴스 객체 생성 및  초기화

class t1 :

    def show(s=1):
        print(f'{s}를 보여줘')

t1.show()


# 이름이 같고, 인스턴스 변수랑 클래스 변수가 있다면
# 