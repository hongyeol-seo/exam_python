# -------------------------------------
# 사람 데이터 타입
# 속성/성질/외모
# 팔/다리
# 눈,코,입
# 혈액형
# 성격
# 이름 
# 키, 몸무게
# 생년월일
# 홍채/지문
# 성별
# 직업
# 나이
# 주민번호
# 핸드폰번호
# 이메일

# 기능/역할/행동
# 말하기
# 걷기
# 공부하다
# 잠자다
# 놀기
# 걷는다
# 생각한다
# 쇼핑한다
# -------------------------------------

#헬스장의 회원관리 프로그램
#건강검진 회원
#동사무소에서 우리 동네 관리 프로그램 
# 이름 / 생년월일/ 성별/ 주소(비공개) /나이(비공개) / 전화번호(비공개) / 주민번호 (비공개) /생애주기
# 기능역할 / jumin

class Jumin:
    
    #클래스 변수 모든 인스턴스 함께 사용 ------------------
    __Dong = "대명동" #외부에서는 비공개 #클래스 내에서는 사용 가능 #생성자 메서드
    
    def __init__(self,name,birth,gender,addr,age,phone,juminNum,lifeCycle):
        self.name = name
        self.__birth = birth
        self.gender = gender
        self.__addr= addr 
        self.__age = age
        self.__phone = phone
        self.__juminNum = juminNum
        self.lifeCycle = lifeCycle

    #getter / setter => 비공개 속성 접근 여부 메서드/ 읽기 기능은 무엇을 줄 것인가!?

    def set__phone(self,phone):
        self.__phone = phone

    def set__addr(self,addr):
        self.__addr = addr

    #비공개 메서드는 없다.

    #일반 메서드 => 인스턴스 메서드
    def allInfo(self):
        print(f'---------[개인정보상세]------------')
        print(f'이   름 {self.name}')
        print(f'주   소 {self.__addr}')
        print(f'주민번호 {self.__juminNum}')
        