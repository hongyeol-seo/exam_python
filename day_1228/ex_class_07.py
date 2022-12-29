# -------------------------------------------------------
# 연산자 산술, 비교, 논리, 멤버, 대입 연산자
# 객체 연산
# list + list
# tuple + tuple
# string + string
# -------------------------------------------------------

# 평면에 점을 나태내는 데이터 타입의 클래스
# x , y => 속성
# 메서드 => 점찍다.
class Point:
    
    #인스턴스 (즉,객체) 속성 생성 및 초기화
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    #인스턴스 메서드
    def drawPoint(self):
        print(f"({self.x},{self.y}) 찍다!")

    def __add__(self,other):

        return self.x + other.x, self.y + other.y


zeroPoint = Point(0,0)
endPoint = Point(50,50)

print(zeroPoint + endPoint)    



# 연산자 오버로딩(overloadring)
# • 객체에서 연산자를 클래스 목적에 맞게 기능 부여 사용
# • 함수이름 앞뒤에 언더스코어(_ _) 두개 연속으로 붙은 함
# +를 한다고 꼭 정수 + 정수 더하는 기능만 있는게 아니라, str인 경우에는 str합치는 기능으로 작동한다.
# % 같은 경우에는 나머지만 나오는게 아니라, 포메팅으로도 쓸 수 있다 =-< 즉 오버로딩