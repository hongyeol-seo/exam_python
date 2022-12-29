#1
class human:
    
    #이름
    #번호
    #주소
    #성별
    #생년월일

    def __init__(self,name,phone,addr,gender,birth):
        self.name = name
        self.phone = phone
        self.__addr = addr
        self.gender = gender
        self.__birth = birth
    
    def set__addr(self,addr):
        self.__addr = addr

    def get_addr(self):
        return self.__addr

    def get__birth(self):
        return self.__birth

#2 
class accout:

    #잔고
    #계좌번호
    #계좌주인
    #주민번호
    #비밀번호
    #은행

    #출금하기
    #입금하기
    #계좌이체하기

    def __init__(self,sum,accNum,ownerName,juminNum,paw,bank,date):
        self.__sum = sum
        self.__accNum = accNum
        self.__ownerName = ownerName
        self.__juminNum = juminNum
        self.__paw = paw
        self.bank = bank
        self.date = date

    def get__sum(self):
        return self.__sum

    def get__accNum(self):
        return self.__accNum

    def get__ownerName(self):
        return self.__ownerName

    def get__juminNum(self):
        return self.__juminNum

    def get__paw(self):
        return self.__paw

    #변경된 비밀번호
    def set__paw(self,paw):
        self.paw = paw

    #출금
    def withdraw(self,outputMoney):
        self.sum -= outputMoney

    #입금
    def deposit(self,inputMoney):
        self.sum += inputMoney