# ----------------------------------------------------------
# 
# 기    능 : 숫자 덧셈 후 결과 반환
# 함 수 명 : getTotal
# 매개변수 : 미정() *nums -> 0개 ~ n개  #입력받는 숫자는 다 더하겠다.
# 반 환 값 : 덧셈결과 
# ---------------------------------------------                                                                                          -------------

def getTotal(*nums):
    #가변 인자들은 튜플 타입으로 들어옴.
    print(type(nums))

# ----------------------------------------------------------
# 기    능 : 숫자 2개 덧셈 후 결과 반환
# 함 수 명 : add
# 매개변수 : a, b
# 반 환 값 : 덧셈결과 
# ---------------------------------------------                                                                                          -------------
# default Value 기본값 : 함수 호출 시 인자를 주지 않는 경우
# 사용되는 값
# 기본값을 가지는 매개변수는 뒷 쪽에 두어줘야한다.
# add(a=0, b) 오류남
def add(b, a=0): 
    # result=a+b
    # return result

    return a+b

# getTotal()
# getTotal(5,3,7,9,10)
# value = add(10,4)
# print(value)
# print(add(11,4))
# print(add(11)) 

# ----------------------------------------------------------
# 기    능 : 숫자 3개 덧셈 후 결과 반환
# 함 수 명 : addThree
# 매개변수 : a, b=5, c=3
# 반 환 값 : 덧셈결과 
# ---------------------------------------------                                                                                          -------------

def addThree(a,b=5, c=3): 
    '''세자리 함수'''
    return a+b+c

#함수사용 -> 호출방법 : 함수명 (인자(파라미터/매겨변수))
# print(addThree(1,5,2),addThree(9),addThree(1,10),addThree(1,c=10))
# 기본값 매개변수가 여러개인 경우는 값 지정시 매개변수 = 값
# ----------------------------------------------------------
# 기    능 : 2개 이상 입력 데이터 덧셈 후 결과 반환
# 함 수 명 : addMore
# 매개변수 : a, b, *nums #가변인자
# 반 환 값 : 덧셈결과 
# ----------------------------------------------------------

# 기본값을 가지는 매개변수는 뒷 쪽에 두어줘야한다.
# 가변인자 매개변수도 뒷 쪽에 두어줘야한다.

def addMore(a,b,*nums):
    result = a + b
    for num in nums:
        result += num
    return result

print(addMore(10,5),addMore(1,2,3,4,5))

# ----------------------------------------------------------
# 기    능 : 회원가입 함수 => 아이디,비밀번호,이메일, 전화번호,[지역, 직업, 나이...]
# 함 수 명 : join
# 매개변수 : id, pw, email, phone, *data
# 반 환 값 : 축하메시지
# ----------------------------------------------------------

def join(id,pw,eamil, phone, **data):
    print(type(data))
    personInfo = {}
    personInfo["id"] = id
    personInfo["pw"] = pw
    personInfo["email"] = eamil
    personInfo["phone"] = phone

    for k,v in data.items() : personInfo[k] = v #한 줄 밖에 없다면, 한 줄에 쓸 수 있다.         
    for k in data.keys():
        personInfo[k] = data[k]

    return personInfo
        
#함수 호출 => (매개변수명 = 값)
#키워드 파라미터가 있는 함수 => 호출 키=값 str타입만 / 
member = join("a123","s1111","a@naver.com","010-85832-8748",joe="student",age=12)

print(f'member => {member}')

# --------------------------------------------
# 함수 타입 => function 클래스
# --------------------------------------------

print(type(join),type(sum))

myFunc = join #주소값을 가지고 있다.

funs = [sum,max,min,join]

print(myFunc("1","2","3","4"),funs[0]([1,2,3]),funs[1](10,-1)) #함수를 리스트에 담아서

#keys() -> #뷰                      \        
#items() -> 리스트의 원소가 tuples타입으로 나옴
#언패킹 : 묶여있는 애들을 풀어서 가져오는데, 담을 공간! 요소의 갯수만큼 변수 필요