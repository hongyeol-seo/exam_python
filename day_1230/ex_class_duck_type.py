# ------------------------------------
# 덕 타이핑(Duck Typing) 동적 -> 일단 변수가 입력이 되어야 할당이 된다.
# 동적타이핑(Dynamic Typing) : 데이터가 저장되어야 타입이 결정됨
# 동적타이핑 방식 중 하나
# 객체의 속성과 메서드를 보고 동적 타입 여부 결정 => "내가 있는 클래스 너도 있니!?"
# ------------------------------------

class A :
    # 클래스 속성
    LOC = "대구"

    #인스턴스 즉 객체 생성 및 초기화
    def __init__(self,name):
        self.name = name

    #인스턴스 즉 객체 메서드
    def play(self,item):
        print(f'{item} 하며 놀고 있다.')

    

class B :
    # 클래스 속성
    LOC = "부산"

    #인스턴스 즉 객체 생성 및 초기화
    def __init__(self,name):
        self.name = name

    #인스턴스 즉 객체 메서드
    def moive(self,item):
        print(f'{item} 영화 재미 있네요.')


class C :

    #인스턴스 즉 객체 생성 및 초기화
    def __init__(self,name):
        self.name = name

    #인스턴스 즉 객체 메서드
    def moive(self,item):
        print(f'{item} 영화 재미 있네요.')



# 함수들 ------------------------
def printMsg(obj):
    print(f'{obj.LOC}출력합니다.')

def doingNow(obj):
    obj.moive("아바타")


aa = A(2022)
bb = B(2023)
cc = C(2025)


#다른 타입의 인스턴스 즉 객체지만, 동일한 속성이 존재하는 경우 
#동일한 함수 사용가능
# printMsg(aa)
# printMsg(bb)
# printMsg(cc) #없으니까 오류 발생

# doingNow(aa)
doingNow(bb)
# doingNow(cc)

#클래스가 10가지 종류가 있는데, 일일히 다가서 aa,bb,cc 무비를 만들어야하는데... 자동으로 실행된다.
#자동으로 데이터를 가지고오자.

