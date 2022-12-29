# -----------------------------------------------
# 연락처 프로그램을 구현하고자 합니다.
# -----------------------------------------------
# 기능 => 연락처 저장 / 삭제 / 수저
# 데이터 => 이름, 전화번호, 사진, 별명, 직장, 그룹, 이메일
# -----------------------------------------------
# (1) 연락처에 사용될 클래스를 생성하세요.
# 

# contact = {}

# contact["010"] = {'name':'hong','email':'hong@naver.com'}
# contact["110"] = {'name':'hong'}
# contact["231"] = {'email':'hong@naver.com'}
# contact["009"] = {}


def savContact(phone, *info):
    #존재 여부 체크
    if phone not in contact:
        contact[phone] = phone
    else :
        print("이미 저장된 연락처입니다.")

# ----------------------------------------------
# 연락처 프로그램 데이터 클래스 => 데이터 타입
# - Member
# - 필수 데이터 => 전화번호, 이름, 이메일
# - 선택 데이터 => 사진, 별명, 주소, 생일
# ----------------------------------------------

class Member:
    #클래스 변수

    #인스턴스 변수 생성 및 초기화 메서드
        def __init__(self,phone,name,email="",alias="",pic="",addr="",birth=""):
            #디폴트
              self.phone = phone
              self.name = name
              self.email = email
              
              self.alias = alias
              self.pic = pic
              self.addr = addr
              self.birth = birth
        
        #인스턴스메서드
        def showInfo(self):
            print(f"---{self.phone}")
            print(f"이  름--- {self.name}")
            print(f"이메일--- {self.email}")
            print(f"별  멸--- {self.alias}")
            print(f"사  진--- {self.pic}")
            print(f"주  소--- {self.addr}")
            print(f"생  일--- {self.birth}")

men = Member("010-8583-8748","hong")
men1 = Member("010-8583-8748","마징가",addr="대구시")
men.showInfo()


class Contact:

    def __init__(self):
        self.member = Member() #멈버객체를 저장?


# ----------------------------------------------------------
# 은행 관리 프로그램
# ----------------------------------------------------------
# - 기능 : 개좌 개설, 해지, 입급 , 출금
# - 데이터 : 계좌번호, 에금주, 개설날짜, 이율, 잔액, 개설지점
# (1) 연락처에 사용될 클래스를 생성하세요. 

#은행 관리 프로그램 데이터 클래스 => 데이터 타입
#Accout
#변수데이터 => 계좌번호, 에금주, 개설날짜, 이율, 잔액, 개설지점, 주민등록번호
#선택데이터 =>
#비공개데이터 => 주민등록번호
#공개데이터 =>

class Acount :
    BANK_NAME = "KB"

    def __init__(self,number,name,date,rate,balance,branch,jumin):
        self.number = number
        self.name = name
        self.date = date
        self.rate = rate
        self.__blance = balance #비공개 데이터 => 클래스 밖에서 사용못함
        self.branch = branch
        self.__jumin = jumin

    #인스턴스 메서드
    def accountInfo(self):
        print(f'예금주----{self.name}')
        print(f'번  호----{self.number}')
        print(f'날  짜----{self.date}')
        print(f'이  율----{self.rate}')
        print(f'잔  액----{self.__blance}')
        print(f'지  점----{self.branch}')
        print(f'주  민 ----{self.__jumin}')


myCount = Acount("000","홍열","1227","1%","1조","대명동","221228")
myCount.accountInfo()
print("공개데이터",myCount.rate)
# print("비공개데이터",myCount.__jumin)
# print(myCount.__blance)
myCount.__blance = 1000000
print(myCount.__dict__)
print(myCount.__blance)