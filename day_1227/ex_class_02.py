# --------------------------------------------------
# 강아지            class dog / name = "메리" /gender = "" / weight = 3.4 / color = "흰색" / def sit() : 코드 / def wait() : / def bark() : 코드 / def tail()
# 이름
# 성별 
# 몸무게 => 변수, 특징, 외형 => 변수 
# 색상
# 앉아
# 기다려
# 짖는다 => 동사 => 함수
# 꼬리친다
# 속성 or 필드 / 멤버변수 / 메서드 / 
# --------------------------------------------------

class Dog: 

    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     pass
    # 이름만 정해준 것이랑 빌트인 함수랑 다르다.

    # 생성자 메서드 : 힙(메모리)에 생성되는 객체 초기화, 데이터 저장
    # self는 주소 
    # 클래스 속성(모든 강아지가 가지고 있는 속성) <=> 인스턴스 변수, 속성(각각의 강아지가 가지고 있는 속성)
    
    legs = 4 #Dog 클래스로 생성된 모든 인스턴스가 함께 사용한다. #클래스변수 

    def __init__(self,name,weight,color):
        print("Dog __init___()")
        self.name = name
        self.weight = weight
        self.colors = color
        # self.legs = 4 #모든 Dog가 공통적으로 가지는 속성/ 데이터
        print(self)

    def bark(self):
        print(f"{self.name}가 짖는다.")

    def tail(self):
        print(f"{self.name}가 꼬리친다")

    def eat(self,*food):
        print(f'{self.name}가 {food}를 먹는다.')

# 객체 생성 ---------------
# 변수명 = 클래스명() / 컨트럭트 메서드 (생성자)
myDog = Dog("Merry",4,"white")
# myDog.bark()
yourDog = Dog("똘똘이",10,"검은색")
broDog = Dog("레오",8,"얼룩이")
# 안불렀는데, 자동으로 불리는 함수 / callback 함수

# 변수명.속성명
# 읽기 => 변수명.속성명
print(myDog.name, myDog.weight, myDog.colors)
# 쓰기 => 변수명.속성명 = 새로운 값
myDog.weight = 5.2
print(myDog.name, myDog.weight, myDog.colors)

#클래스변수
myDog.legs = 6
print(myDog.legs, Dog.legs)
print(yourDog.legs)
#재사용
#중복

#객체(인스턴스) 메서드 사용
myDog.bark()
yourDog.tail()
broDog.eat("개고기","양고기")


