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

# 11. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.

#시작 구구단 종료구구단

check = True
strNum =2 
endNum = 4
endNum2 = endNum + 1 
dan = 1 

while check :
    if check or strNum < endNum2:            
        if check and dan <= 10 :
            print(f'{strNum} * {dan} = {strNum * dan}')
            dan +=1
        
        elif check and dan == 10:
            print("a")
            dan = 1
            strNum +=1
        
        if strNum >= endNum2:
            print("b")
            check = False
            break

    else :
        print("c")
        check = False
        break

    
