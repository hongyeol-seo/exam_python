#코드 #실행여부
#1 

n = int(input("출력 원하는 단 입력 : "))
result = [n*i for i in range(1,10)]

for j in range(1,10):
    if j % 5 == 0:
        
        print(f"{n} * {j} = {result[j-1]}","\t")

    else :
        print(f"{n} * {j} = {result[j-1]}",end="  ")

#2

def addData(*datas):
    if len(datas) > 0:
        # print(datas, type(datas))
        arr = list(datas)
        sum = 0
        if isinstance(arr[0], str):
            sum = ""
            for i in datas:

                sum += i
        else:
            for i in datas:

                sum += i
        print(sum)

    else:
        print("None")


addData()
addData(1, 3, 5)
addData(True, True, False, False, True)
addData(0.9, 12.4, 4.1)


#3 

datas = {"과목" : {"국어","수학","윤리","국사"},"베트맨":[90,89,98,99],"마징가":[82,73,71,91],"피오나":[78,99,91,83]}

name = list(datas.keys())
print(name)

print(f"{name[1]} 최고점수 {max(datas[name[1]])},'국사', 최저점수{min(datas[name[1]])},'수학'")
print(f"{name[2]} 최고점수 {max(datas[name[2]])},'국사', 최저점수{min(datas[name[2]])},'윤리'")
print(f"{name[3]} 최고점수 {max(datas[name[3]])},'수학', 최저점수{min(datas[name[3]])},'국어'")

#4
def birth(datas):
    year = datas[0:2]
    newYear = "20"+year
    month = data[2:4]
    day = datas[4:6]
    gender = datas[7]
    age = 22-int(year)+1
    starloc = ""
    if gender == 3 :
        newGender = "남자"

    else :
        newGender = "여자"

    if int(month) == 1 or  int(month) == 2:
        starloc = "물병자리"

    elif int(month) == 3 or int(month) == 4:
        starloc = "양자리"

    elif int(month) == 9 or int(month) == 10:
        starloc = "물병자리"

    print(f"{age}세 {newGender} {newYear}년 {month}월 {day}일 {starloc}")

data = input("주민등록번호 입력 : (000000-000000) : ")
birth(data)

#5

def menu():
    print("-"*20)
    print("1. 입력")
    print("2. 대문자")
    print("3. 소문자")
    print("4. 코드화")
    print("5. 코드화")
    print("-"*20)

check = False

while True :

    menu()
    
    msg = int(input("메뉴 선택(1~5) : "))

    if msg == 1:
        data = input("영어 입력 : ")
       
    elif msg == 2 :
        #대문자
        print(data.upper())

    elif msg == 3 :
        #소문자
        print(data.lower())

    elif msg == 4:
        #코드화
        for i in data:
            print(ord(i),end="")

        print("")
        
    elif msg == 5:
        print("영어 변환기 프로그램을 종료합니다.")
        break