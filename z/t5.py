#1 

# j = 5 #입력값
# temp = [[j , i , j*i ] for i in range(1,10)]

# for i in temp:
#     if i[1] % 5 == 0 :
#         print(f'{i[0]} * {i[1]} = {i[2]}', end="\n")
    
#     else : 
#         print(f'{i[0]} * {i[1]} = {i[2]}', end="\t")
    

#2
def addDate(*data):
    if len(data) > 0 :
        num = 0
        for i in data:
            num += i
    # else : 
    #     return None

    return num

# def addDate(*nums):
#     total = 0
#     for num in nums :
#         total += num

#     return total if len(nums)>0 else None
#     #조건부 표현식

print(addDate())
print(addDate(1,3,5))
print(addDate(True, True, False, False, True))
print(addDate(0.9, 12.4, 4.1))

#3 

datas = {"과목" : ["국어","수학","윤리","국사"],"베트맨":[90,89,98,99],"마징가":[82,73,71,91],"피오나":[78,99,91,83]}

name = list(datas.keys())

num1 = datas["과목"][datas[name[1]].index((max(datas[name[1]])))] #베트맨 최고의 과목
num2 = datas["과목"][datas[name[1]].index((min(datas[name[1]])))] #베트맨 최저의 과목

num3 = datas["과목"][datas[name[2]].index((max(datas[name[2]])))] #마징가 최고의 과목
num4 = datas["과목"][datas[name[2]].index((min(datas[name[2]])))] #마징가 최저의 과목

num5 = datas["과목"][datas[name[3]].index((max(datas[name[3]])))] #피오나 최고의 과목
num6 = datas["과목"][datas[name[3]].index((min(datas[name[3]])))] #피오나 최저의 과목

print(f"{name[1]} 최고점수 {max(datas[name[1]])},{num1}, 최저점수{min(datas[name[1]])},{num2}")
print(f"{name[2]} 최고점수 {max(datas[name[2]])},{num3}, 최저점수{min(datas[name[2]])},{num4}")
print(f"{name[3]} 최고점수 {max(datas[name[3]])},{num5}, 최저점수{min(datas[name[3]])},{num6}")

#4 

def birth(year, month, day, gender):

    year = int(year)
    age = 2022 - year + 1 
    tii = ["원숭이","닭","개","돼지","쥐","소","호랑이","토끼","용","뱀","말","양"]
    newtii = tii[year % 12]

    month = int(month)
    day = int(day)
    gender = int(gender)
    if gender == 1 or gender == 3 :
        newgender = "남자"
    else :
        newgender = "여자"    

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        starloc = "물병자리"

    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        starloc = "물고기자리"

    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        starloc = "양자리"

    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        starloc = "황소자리"

    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        starloc = "쌍둥이자리"

    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        starloc = "게자리"

    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        starloc = "사자자리"

    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        starloc = "처녀자리"

    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        starloc = "천칭자리"

    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        starloc = "전갈자리"

    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        starloc = "궁수자리"

    elif (month == 12 and day >= 25) or (month == 1 and day <= 19):
        starloc = "염소자리"

    print(f"{age}세 {newgender} {year}년 {month}월 {day}일 {starloc}, {newtii}")


    # print(year,month,day,gender)


str = "920413-1008910"
str = "011010-3234567"

headnum, backnum = str.split("-")
year = headnum[0:2]
month = headnum[2:4]
day = headnum[4:6]
gender = int(backnum[0])

if gender == 1 or gender == 2:
    year = "19" + year

else:
    year = "20" + year


birth(year, month, day, gender)

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
            print(hex(ord(i)),end="")

        print("")
        
    elif msg == 5:
        print("영어 변환기 프로그램을 종료합니다.")
        break