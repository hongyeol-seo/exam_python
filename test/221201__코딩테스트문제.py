# 1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을 출력하는 함수를 구현하세요.

def sortArr(arr):
    arr.sort(reverse=True)
    print('가장 높은 문자열 : {}, 가장 낮은 문자열 : {}'.format(arr[0],arr[-1]))

msg=['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']

sortArr(msg)

# msg.sort(reverse=True)
# print('가장 높은 문자열 : {}, 가장 낮은 문자열 : {}'.format(msg[0],msg[-1]))

# 2. 문자열을 입력하면 UTF-8로 인코딩된 값을 아래와 같이 출력된 함수를 구현해 주세요.

def printStr(n):
    for i in n:
        print(hex(ord(i)),end="")

    print("")

    for j in n:
        print(bin(ord(j)),end="")

printStr("가나다")

data = "가나다"

print(hex(ord("가"))+hex(ord("나"))+hex(ord("다")))
print(bin(ord("가"))+bin(ord("나"))+bin(ord("다")))

#3. 숫자와 콤마로만 이루어진 문자열 data가 주어진다. 이때, data에 포함되어있는 자연수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
# 함수를 구현하세요!

def printData(m):
    im = list(m.replace(",",""))
    for i in range(len(im)):
        im[i] = int(im[i])

    print('{}의 합 : {}, 가장 큰 수 {}, 가장 작은 수 {}'.format(m, sum(im),max(im),min(im)))

printData('123,42,98,18')


data='123,42,98,18'
data = list(data.replace(",",""))

for i in range(len(data)):
    data[i] = int(data[i])

print('123,42,98,18의 합 : {}, 가장 큰 수 {}, 가장 작은 수 {}'.format(sum(data),max(data),min(data)))

data="1,234"
data=list(data.replace(",",""))
for i in range(len(data)):
    data[i] = int(data[i])

print('1,234의 합 : {}, 가장 큰 수 {}, 가장 작은 수 {}'.format(sum(data),max(data),min(data)))

# 4. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는 게임으로 아래 조건을 만족하도록 구현하자.

n = 100

for i in range(1,n+1):

    count = 0
    for j in str(i):
        if "2" in j or "4" in j or "8" in j :
            count+=1
            
    if count >= 1:
        if i % 20 == 0:
            print("#", end="\n")
        else:
            print("#", end=" ")        
    else :
        if i % 20 == 0:
            print(i,end="\n")
        else :
            print(i,end=" ")

#5. 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요

# month = int(input("좋아하는 월 입력 : "))
month = 15

monDict = {1:["Jan.","Winter"],
2:["Feb.","Witer"],
3:["Mar.","Spring"],
4:["Apr.","Spring"],
5:["May","Spring"],
6:["Jun.","Summer"],
7:["jul.","Summer"],
8:["Aug.","Summer"],
9:["Sep","autumn"],
10:["Oct","autumn"],
11:["Nov","autumn"],
12:["Dec.","Winter"]}

if month in monDict :
    for i in monDict[month]:
        print(i,end=" ")

else :
    print("존재하지 않는 월입니다.")

# 6. 숫자와 화폐단위를 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요

data = "   1234567,  $"

data = data.strip()
print(data)
data = data.replace(" ","")
data = data.replace(",","")
won = data[-1]
print(format(int(data[:-1]),","),end="")
print(won)

# 7. 입력받은 정수에 대한 약수를 출력하는 함수를 만들어 주세요.

def measure(n):
    arr = []
    for i in range(1,n+1):
        if n%i == 0 :
            arr.append(i)
    print(f'{n}의 약수 : {arr}')

measure(int(input("구하고 싶은 수 : ")))


# 8. 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.

msg = ""

msg = "Happy New Year 2023!"
arr = set()
for i in msg:
    if i.isdecimal():
        print(i)
        arr.add(int(i))

for j in arr:
    print(j, end=" ")

# while msg != "X" or msg != "x":

# 9. 생일을 입력 받은 후 한국 나이, 외국 나이를 알려주는 함수를 생성해 주세요.
    data = "2000.07.01."
    data = "2000.12.29."

    data = data.replace(".","")
    year = data[:4]
    month = int(data[4:6])
    day = int(data[7:])
    print(year, month, day)

import datetime
dt_now = datetime.datetime.now()

print(dt_now)
print(type(dt_now.year))
print(dt_now.month)
print(dt_now.day)
# https://somjang.tistory.com/entry/BaekJoon-16199%EB%B2%88-%EB%82%98%EC%9D%B4-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0-Python

# 팩토리얼(Factorial)을 while반복문으로 구현해 주세요. 팩토리얼 수를 입력 받아서 팩토리얼 결과를 아래와 같이 출력하세요.

inputNum = 7
num = 0 
check = True

while check :
    if inputNum == 0 :
        check = False
        continue
    
    print(str(inputNum)+"! =>", end="")
    while check:
        if inputNum == 0:
            check = False
            continue

        num *= inputNum
        inputNum -= 1
        print(inputNum, end=" ")
        if inputNum != 1 and inputNum != 0:
            print("*", end=" ")
        
    print("=",num)

# 13. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.

#시작 구구단 종료구구단


def gugudan(s,e):

    check = True
    strartNum = s
    newStr = strartNum
    endNum = e
    num = 1

    while check:
        if newStr <= endNum and num < 10: 
            print(f"{newStr} * {num} = {newStr*num}", end="\t")
            newStr +=1 
            continue

        elif newStr > endNum and num < 10:
            print("")
            newStr = strartNum
            num += 1
            continue

        else :
            check = False
            #break

gugudan(2,6)
    



check = True 
incheck = True #출력체크여부
num = 7 #입력값 
checkNum = num
sum = 1 #합계저장

while check :

    if num == 0:
        print(f'{num}! => {num}')
        check = False
        continue
    elif num >= 1 and incheck :
        print(f'{num}! =>',end=" ")
        incheck = False
        continue
    elif checkNum >= 1 :
        if checkNum > 1 :
            print(checkNum, "*", end=" ")
            sum *= checkNum 
            checkNum -= 1
            continue
        else :
            print(checkNum,end=" ")
            sum *= checkNum 
            checkNum -= 1
            continue

    else :
        print(f"= {sum}")
        break
        
# 11. 입력받은 숫자 범위 안에서 소수(Prime Number)를 찾아서 반환하는 함수를 생성하세요.

# 입력은 함수에 포함하지 않음
# - 소수(Prime Number)란? 1보다 큰 수 중 1과 자기 자신만을 약수로 가지는 수

n=10

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  
  return True

for i in range(n+1):
  if(isPrime(i)):
    print(i)


#12. 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수 출력하세요.

data = {"국어":[90,82,77,94,78],"수학":[89,71,100,82,99],"윤리":[98,80,92,93,91],"국사":[99,91,90,71,83]}

arr= list(data.keys())

print(f'[{arr[0]}] 최고점수 : {max(data[arr[0]])}, 최저점수`{min(data[arr[0]])}')
print(f'[{arr[1]}] 최고점수 : {max(data[arr[1]])}, 최저점수`{min(data[arr[1]])}')
print(f'[{arr[2]}] 최고점수 : {max(data[arr[2]])}, 최저점수`{min(data[arr[2]])}')
print(f'[{arr[3]}] 최고점수 : {max(data[arr[3]])}, 최저점수`{min(data[arr[3]])}')


# 14. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.

n = 12345

num = len(str(n))

if num == 5:

printf(" 천의 자리 : %d \n" , num/1000);
num = num % 1000;
printf(" 백의 자리 : %d \n" , num / 100);
num = num % 100;


n = 12345
print("만의자리 : {}".format(int(n/10000))) if n/10000 > 1 else True
print("천의자리 : {}".format(int(n/1000)/10)) if (n%10000)/1000 > 1 else True





print("백의자리 : {}".format(int(n/100))) if n/100 > 1 else print("패스")

a = 123
print("백의자리 : %d\n"%(a/100))
print("십의자리 : %d\n"%((a%100)/10))
print("일의자리 : %d\n"%(a%10))



# 11. 아래 그림처럼 나오도록 코드 작성하세요. 가장 긴 라인의 별의 수는 15개,
#  전체 라인수도 15라인 입니다.

for i in range(8):
    print("{:^15}".format("*"*(2*i+1)))
for i in range(7):
    print("{:^15}".format("*"*(13-2*i)))

for i in range(1,17,2) :
    print("{0:^15}".format("*" * i))

print("{0:^15}".format("*" * 4))
print("{0:^15}".format("*" * 4))
print("{0:^15}".format("Merry Christmas"))
print("{0:^15}".format("2023"))

# 17. 문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자로
# 변환하여 출력하는 코드를 구현하세요.

data = 'Merry Christmas HaPPy New YEaR'

print(data.swapcase())

#18. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이출력해 주세요.


#19. 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.

def saveInfo(**datas):
    for key in datas.keys():
        print(f"{key} => {datas.get(key)}")

saveInfo(age=12, phone='010-2222-1111',job='학생', loc='대구')




# def saveInfo(**infos):
#     print(type(infos), len(infos), infos)
#     for k,v in infos.items():
#         print(f'{k}-{v}')

#     for key in infos.keys():
#         print(f'{key} => {infos.get(key)}')




#20 [나의 계산기] 프로그램을 구현하세요.

def choice():
    print("1. 입력",end="  ")
    print("2. 덧셈",end="  ")
    print("3. 뺄셈",end="\n")
    print("4. 곱셉",end="  ")
    print("5. 나눗셈",end="  ")
    print("6. 종료",end="\n")

isCheck = False
while True :
    
    choice()
    data = input("메뉴선택 (1~6) : ").strip()
    
    if data == "6": #종료
        print("나의 계산기 프로그램을 종료합니다.")
        break

    elif data == "1": #입력
        if isCheck == False :
            nums = input("숫자 2개 입력 : ").strip()
            n1, n2 = nums.split(",")
            n1, n2 = int(n1), int(n2)
            isCheck = True
        
        else :
            print("입력된 값이 있습니다.")

    elif data == "2":
        if isCheck:
            print(f"{n1} + {n2} = {n1+n2}")
        else :
            print("입력된 데이터가 없습니다.")

    elif data == "3":
        if isCheck:
            print(f"{n1} - {n2} = {n1-n2}")
        else :
            print("입력된 데이터가 없습니다.")
    
    elif data == "4":
        if isCheck:
            print(f"{n1} * {n2} = {n1*n2}")
        else :
            print("입력된 데이터가 없습니다.")
    
    elif data == "5":
        if isCheck:
            print(f"{n1} / {n2} = {n1*n2}")
        else :
            print("입력된 데이터가 없습니다.")

    else:
        print("메뉴 선택값이 없습니다.")
