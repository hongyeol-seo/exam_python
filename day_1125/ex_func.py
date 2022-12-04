# --------------------------------------
# 복잡한 함수 => 활용도 높고 많이 사용됨
# --------------------------------------

def addTwo(n1,n2):
    return n1+n2

# 숫자 5개 더하는 함수
def addFive(n1,n2,n3,n4,n5):
    return n1+n2+n3+n4+n5

# 숫자 4개 더하는 함수
def addFour(n1,n2,n3,n4):
    return n1+n2+n3+n4

# 굳이 여러개를 만들 필요가 있을까?
# 매개변수에 수가 인자의 수를 유동적으로 처리하는 함수
# => 가변인자 함수
# => 매개변수의 형태: *변수명
# => 매개변수에 전달되는 인자 갯수 : 0개  ~ n개

# 대표적인 것
print()
print(10)
print(1,2,3,4,5,6,7) #*values #가변인자

# 숫자 4개 더하는 함수
# 기능 : 입력된 데이터를 모두 더하는 기능
# 함수명 : addData
# 매개변수 : *datas
# 반환값 :덧셈 결과

def addData(*datas):
    # set은 중복이라서 X
    # dict는 키 값이라서 X
    # print(type(datas),len(datas))
    if len(datas) > 0 :
        total ="" if isinstance(datas[0],str) else 0 #조건부 표현식
    # total = 0
    #int로 만든 객체를 인스턴스라고한다. #이게 인스턴스이니?
    
    for data in datas :
        total +=data
    return  total

# addData()
# addData(1,3,5)
print(addData(10))
print(addData("a","b","c","d")) #total = 0 무조건 정수일때 #타입을 확인해야한다.
print(addData(True,True,False,False,True)) #3

print(isinstance(5,int)) #5는 int의 인스턴스이니?
print(isinstance(5,str)) #5는 str의 인스턴스이니?
print(isinstance("5",str)) #'5'는 str의 인스턴스이니?

# 입력된 숫자를 계산해주는 기능
# 함수명 : calcNum
# 매개변수 : *nums  변인자 숫자

def calcNum(how,*nums):
    if how =="+":
        print("덧셈")
    if how =="-":
        print("뺄셈")
    if how =="*":
        print("곱셉")


calcNum("+",10,20)
# calcNum() #뒤에있는 것은 없어도, 앞에 *표시인것은 있어야한다.

# 입력된 숫자를 계산해주는 기능
# 함수명 calc
# 매개변수 : 
# 반환값 : 계산 결과
# 기본값

# def calc(how="+",*num): #만약 디폴트값이 있다면, 생략이 될 수 있기 때문에...
# print(f"how : {how}, num : {num}")

def calc(*num,how="+"): #만약 디폴트값이 있다면, 생략이 될 수 있기 때문에...
    print(f"how : {how}, num : {num}")

calc(11,22,33,how="-")


def add(a,b=0, c=0): #default value!
    return a+b+c

add(3)

add(3,5,7)

#기본값 매개변수 : 함수 호출시, 인자를 주지 않은 경우 사용할 값을 미리 정해둔 매개변수
#형식 : 매개변수명 = 0 
def add(a,b=0,c=0): #non-default argument follows default argument 나는 두개 다 쓰고, 하고 싶은데 #다 내꺼! 
    print(a,b,c)
    print("걸과 : ", a+b+c)

add(3)
add(3,5,7)
#기본값 매개변수가 여러개 있는 경우는 
#값 지정시 함수호시 매개변수 지정
#디폴트 value들은 호출해서 정해서줘야한다.
add(3,c=5) #a는 3 b는 0 c는 5

#별이 2개 키워드 매개변수!
#매개변수 데이터의 의미와 값을 함께 전달
#형식 : 매개변수명 = 값
#기본값 : 매개변수가 여러개 있는 경우는 함수 호출시에 
#숫자랑 문자랑 식별해서 들어온다.
#개인정보를 입력받아 저장하는 함수!
#함수명 : saveInfo

def saveInfo(**infos):

    print(type(infos),len(infos))
    for k,v in infos.items() : #튜플로 묶여있는 애들을 언패킹해서 받는다.
        # print(f'{key} =>')
        print(f'{k}-{v}')
#키워드 파라미터 함수 호출 방법 
#함수명(변수명 = 값, ...., 변수명 )
saveInfo(name="Hong")
saveInfo()
saveInfo(age=12, phone='010-222-1111',job='학생',loc="대구") #데이터의 의미와 값을, 같이 준다. / 사람마다 입력하는 내용이 다 다르기 때문에
#키워드 파라미터!

#반환값을 건드린다!
#나는 한번에 4개의 결과값을 받고싶다.
#반환값을 여러개 돌려주는 함수!
#사칙연산 수행후 결과를 반환하는 함수!
# fourCalc
# 매개변수는 가변인자로 하고싶지만, 복잡할 것 같으니까!
# 반환값 : 덧셈, 뺄셈, 곱셉, 나눗셈!

def fourCalc(num1, num2):
    addValue = num1 + num2
    minValue = num1 - num2
    mulValue = num1 * num2
    divValue = num1 / num2 if num2 > 0 else 0

    return addValue,minValue,mulValue,divValue #튜플 #수정을못하니까 #

#*가변 **가변키워드 파라미터

# ---------------------------------------

