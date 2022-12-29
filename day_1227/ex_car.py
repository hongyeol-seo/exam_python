class Motorcycle :

    weight = 270

    def __init__(self,name,oil,color):
        self.name = name
        self.oil = oil
        self.color = color
        print("시동을 겁니다")

    def drive(self,speed):
        self.speed = speed
        print(f'{self.name}가 {speed}의 속도를 냅니다.')

    def stop(self):
        print(f'{self.name}가 멈춥니다.')

    def bright(self):
        print(f'{self.name}가 불을 비춘다.')

    def turn(self, where):
        print(f'{self.name}가 {where} 뱡향으로 회전합니다.') 

    def accident(self):
        #충격파
        print(f'{self.weight * self.speed}의 힘으로 박치기')

    def __del__(self):
        pass #소멸자
myMotocycle = Motorcycle("나의오토바이",100,"black")
yourMotocycle = Motorcycle("너의오토바이",20,"red")

myMotocycle.drive(100)
myMotocycle.stop()
myMotocycle.bright()
myMotocycle.turn("오른쪽")
myMotocycle.accident()

#클래스변수
#인스턴스변수
#시스템메서드
#메서드                   ``

# 인스턴스와 클래스

#매직매서드 / 매직변수(매직어트리뷰트)

# print(myMotocycle.__dict__) #인스턴스가 가지고 있는 속성값을 알 수 있다.
# print(myMotocycle.__dir__)
# print(myMotocycle.__class__) 

for item in Motorcycle.__dict__.items():
    print(item)


# 객체지향 언어 
# 유지보수쉽게
# 정보은닉 / 캡슐화 
# 상속(재사용)
    # 1개 자바에서는 다중 상속 못하게 만들어놨다. 파이썬은 다중상속을 허용한다. 단일상속 vs 복수상속 oop
    # 모든 클래스, 오브젝트 클래스 / 오브젝트가 가지고 있는 __애들을 전부 다 가지고 있다.
# 다형성 / 재사용


#정보은닉 : 
#클래스 안에 들어있는 필드, 파이썬 정보은닉 X 제공안함 대신 __ 붙이면 비공개로 하겠다. / __메소드도 마찬가지

