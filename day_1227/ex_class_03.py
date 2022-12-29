# ----------------------------------
# 
# ----------------------------------

num1 = [1,2,3,4]
num2 = [1,1,2,1]
msg = "Good"
greeting = "2023"

#연산 #덧셈, 곱셉, 나머지 

num3 = num1 + num2
data = msg + greeting

print(num3)
print(data)

num4 = num1 * 3 #반복
data1 = msg * 3 #반복
print(num4, data1)

# ----------------------------------
# Point 클래스
# 변수
# 클래스 변수 => color
# 인스턴스 변수 => x, y 
# 메서드 
#       시스템 메서드(생성자 메서드) => __init__() : 인스턴스 변수 생성 및 초기화\
#       비공개속성 Getter/Setter => 비공개 속성 값 읽기, 쓰기 메서드
#       비공개 메서드 -> 없음 def __method():
#       커스텀 메서드 -> def print point()
# 
# ----------------------------------

class Point:
    
    color = "blue"

    def __init__(self,x,y):
        #인스턴스 변수 생성 및 초기화
        self.x = x
        self.y = y

    #메서드
    def printPoint(self):
        print(f"({self.x},{self.y})")

    #덧셈이 들어갈 때, 자동적으로 호출되는 콜백함수
    def __add__(self,other):
        print("__add()__()")
        return self.x + other.x, self.y + other.y

    def __add__(self,other):
        print("__add()__()")
        return self.x + other.x, self.y + other.y

    def __sub__(self,other):
        print("__sub()__()")
        return self.x - other.x, self.y - other.y

#객체 생성
p1 = Point(10,10)
p2 = Point(5,5)
p3 = Point(0,0)

p1.printPoint()
p2.printPoint()

#객체 연산 ----------------------------------------------------------

print(f'p1 + p2 {p1 + p2}') 
print(f'p1 - p2 {p2 - p1}') 
#객체 객체 연산 시켜지면 / 더 하기를 수행할 메서드가 있는지
#상황이 맞을 때 
