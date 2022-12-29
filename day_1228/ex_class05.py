# (1) 어떤 클래스 => 클래스 클래스명
# (2) 특징/성격/외형/속성들 => 변수 속성(attribute),필드(field)
# (3) 기능/역할/행동  => 클래스 전용 함수 메서드(Method)
# ------------------------------------
# 휴대폰 클래스
# ------------------------------------
# 전화
# 앱, 배터리, 번호, 문자보내기, 브랜드, 제조사
# 사진, 음악, 네비게이션, 날씨
# 웹서핑하다, 사진찍다. 전화하다.     
# 폴더 형태, 크기, 

# 절차지향 / 객체지향

# class Phone:

#     #클래스 변수
#     maker = "SANSUNG"

#     #인스턴스 속성 생성 및 초기화
#     def __init__(self,number,color):
#         self.number = number
#         self.color = color

    
#     #인스턴스 메서드
#     def calling(self, phoneNumber):
#         print(f"{phoneNumber}에 전화합니다.")

    
#     def mms(self,message):
#         print(f'{self.number}가 {message}를 발송합니다.')

# n1 = Phone("010","pink")
# n2 = Phone("011","Yello")
# print(n1.maker)

# --------------------------------
# BMI 지수 => 키와 몸무게로 계산
# --------------------------------

class A :
    
    # 속성 2개 가지는 클래스
    def __init__(self,weight,height,bmi):
        self.__weight = weight
        self.__height = height
        self.bmi = bmi

    def get__weight(self):
        return self.__weight

    def sssssset__weight(self,weight):
        self.__weight = weight
        # return self.__weight
        self.____showinfo()

    def ____showinfo(self):
        print("=======")
        print(self.__weight,self.__height)
        print("=======")
    def __cal(self):
        self.BMI = self.__weight/((self.__height/100)*(self.__height/100))

# 인스턴스 (즉 객체 ) 생성 ------------------
# 변수 = 클래스명()
myM = A(95,185," ")

# 인스턴스속성 확인 => 변수명, 속성명
# print('my.bmi => ',myM.bmi)
# print('my.weight => ',myM.__weight)
# print('my.get__weight => ',myM.get__weight())
print(myM.sssssset__weight(50))
# myM.____showinfo()


