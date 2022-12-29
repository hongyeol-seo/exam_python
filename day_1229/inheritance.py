# ----------------------------------------
# 상속(Inhertance) : 재사용 및 기능확장
# ----------------------------------------

# ----------------------------------------
# 포인터를 나타내는 데이터 타입 => 클래스
# - 속성/필드
# - 좌표(10,5)
# - 기능/역할
# - 점찍기
# 동그라미 그리기
# 별그리기
# ----------------------------------------

class P2D :

    #클래스 변수

    #인스턴스 생성 및 변수 초기화 메서드

    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("하이")

    #인스턴스 메서드
    def pointting(self):
        print(f'({self.x},{self.y} 위치에 점찍기)')

    def drawCircle(self,color):
        print(f'({self.x},{self.y} 위치에 {color} 색상 동그라미 그리기)')

    def drawStar(self,action):
        print(f"{self.x},{self.y} 위치에 {action} 별 그리기")

    # 인스턴스 (즉 객체) 생성하기 => 클래스명(매개변수) : __init__ 메서드랑 갯수 같아야함


class P3D :

    #클래스 변수

    #인스턴스 생성 및 변수 초기화 메서드

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    #인스턴스 메서드
    def pointting(self):
        print(f'({self.x},{self.y},{self.z} 위치에 점찍기)')

    def drawCircle(self,color):
        print(f'({self.x},{self.y},{self.z} 위치에 {color} 색상 동그라미 그리기)')

    def drawStar(self,action):
        print(f"{self.x},{self.y},{self.z} 위치에 {action} 별 그리기")

    # 인스턴스 (즉 객체) 생성하기 => 클래스명(매개변수) : __init__ 메서드랑 갯수 같아야함


class Point3D(P2D):
    #상속관계 사용되는 키워드 supoer
    #인스턴스 속성 초기화
    def __init__(self, x, y,z):
        super().__init__(x, y)
        # super().drawCircle("빨간색")
        self.x = x+10000
        print(f'#####{self.x}')
        # print(f"@@@@{super().x}") 
    
    # def drawCircle(self,color):
    #     print(f'({self.x},{self.y},{self.z}) 위치에 {color} 색상 동그라미 그리기)')

    #부모 클래스로부터 상속 받은 메서드와 구현 부분을 변경 -=> 오버라이딩()
    #메서드명. 매개변수


# bluePoint = Point2D(20,4,5)
# bluePoint.drawCircle("파란색") 
# bluePoint.drawStar("반짝반짝")

pinkPoint = Point3D(10,5,3)
pinkPoint.drawCircle("pink")

