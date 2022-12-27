# ----------------------------------------------------------------------------
# 바둑알이 놓이는 위치 저장 클래스
# 클래스명을 : Point
# 변수 :
#       클래스 변수 :
#       인스턴스 변수 : x(공개용속성0), __y(비공개용속성)
# 메서드 
#       - 시스템 메서드 : __init__()
#       - 커스텀 메서드 : put(), show()
#       - getter/setter 비공개 속성의 값 읽기/쓰기
#       - get속성명(), set속성명()
# ----------------------------------------------------------------------------

class Point():
    #클래스 속성

    #인스턴스 속성 초기화 및 생성 메서드 => 생성자 메서드

    def __init__(self, x, y ):
        self.x = x
        self.__y = y

    #메서드 
    def put(self):
        print(f"({self.x},{self.__y}) -- o")

    def get__y(self):
        return self.__y

    def set__y(self, y) :
        self.__y = y

#인스턴스 생성
p1 = Point(10,5)
# p1.__put() #Point' object has no attribute '__put'
# print(p1.__y) #AttributeError: 'Point' object has no attribute '__y'

p1.__y =12312312
print(p1.__y)
p1.put()
print(p1.__dict__)


# print(p1.__y)

# __어떤 툴은 안보이고, 또 어떤 툴은 안보인다.

#비공개로 되어있는 데이터는 어떻게 변경을 할 수 있는지?

# p2=Point(5,5)
# print(p1.__dict__)
# print(p2.__dict__)

p1.z = 17 #불법 증축!
# p1.__z = "a" #원래는 없던 속성인데 / 인스턴스 생성 후 추가된 속성
# p1.__z = 200 #비공개라고 표시되어있지만, 변경되는 것에는 상관없다.
print(p1.__dict__)
# print(p2.__dict__)

# p1.set__y(50) #비공개속성 쓰기
# p1.put()

# print('p1.__y : ',p1.get__y()) #비공개속성 읽기   

# #오버로딩 / 매개변수 . 타입, 순서가  다른 함수 정의 / 
# #add(int) vs add(float) / def add(int,int) vs add(int, float)
# #안에 내용물은 내가 짠다?

# #오버 라이딩 / 상속관계에 있을 때, 내 입맛에 고친것. 
# # (함수명도, 매개변수도 변경해서는 안된다. 단 내용물만 바꿀 수 있따.)