# 1
# 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을 출력하는 함수를 구현하세요.
# 입력 msg=[‘Good’, ‘child’, ‘Zoo’, ‘apple’, ‘Flower’, ‘ zero’]
# 출력 정렬 결과 : ['zero', 'child', 'apple', 'Zoo', 'Good', 'Flower'
#                 가장 높은 문자열 : zero, 가장 낮은 문자열 : Flower
A=input('생각나는 단어들을 입력하시오.(,로 구분) : ').strip()
AA=A.split(',')
AAA=sorted(AA, reverse=True)
print(f'정렬 결과 : {AAA}')
print(f'가장 높은 문자열 : {AAA[0]}, 가장 낮은 문자열 : {AAA[-1]}')


print('----------------------------------------------------------')
# 2
# 문자열을 입력하면 UTF-8로 인코딩된 값을 아래와 같이 출력된 함수를 구현해 주세요.
# 입력 data=“가나다”
# 출력1 "가나다"의 인코딩 : 0xac000xb0980xb2e4  - 16진수 
# 출력2 "가나다"의 인코딩 : 0b10101100000000000b10110000100110000b1011001011100100" - 2진수
B=input('단어를 입력하시오. : ')
BB=B.encode('utf-8')
print(f'"{B}"의 인코딩 : {BB}')


print('"가나다"의 인코딩(16진수) :',hex(ord('가'))+hex(ord('나'))+hex(ord('다')))
print('"가나다"의 인코딩(2진수) :',bin(ord('가'))+bin(ord('나'))+bin(ord('다')))

data=input('단어입력 : ')
data=list(data)

for i in data:
    print(bin(ord(i)),end='')   
print()
for i in data:
    print(hex(ord(i)),end='')
print()



# chr(코드) => 코드에 해당하는 문자 반환
# ord(문자1개) => 문자에 해당하는 코드 반환
# hex(10진수) => 16진수로 변환
# bin(10진수) => 2진수로 변환


print('----------------------------------------------------------')
# 3
# 숫자와 콤마로만 이루어진 문자열 data가 주어진다. 이때, data에 포함되어있는 
# 자연수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
# [입 력] data=‘123,42,98,18’
data='123,42,98,18'

dataa = []
for num in data:
    if num.isdigit():
        dataa.append(num)   # dataa.append(int(num)) 이 더 편함
dataaa=list(map(int,dataa))

print(f'"123,42,98,18"의 합 : {sum(dataaa)}, 가장 큰 수 : {max(dataaa)}, 가장 작은 수 : {min(dataaa)}')
# import = 외부함수 불러오기
# re 함수 = 숫자 찾기, 문자 찾기, 패턴 찾기 등등 쓸 수 있음
# re.findall = 규칙에 해당되는 데이터들을 추출하는 함수
# r'\d+'는 1회 이상 반복되는 숫자들에 대한 패턴을 의미합니다.
# r'\d'는 1개씩 추출

print('----------------------------------------------------------')
# 4
# 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
# 게임으로 아래 조건을 만족하도록 구현하자
# 조건 1 : 숫자를 int형 타입으로 input함수를 이용하여 입력받는다
# 조건 2 : 2, 4, 8 숫자가 있을 경우 #을 나타나게 한다
# 조건 3 : 입력받은 숫자가 1000일 경우 1부터 1000 까지에 해당하는 2, 4, 8을 #으로 출력한다.
# 조건 4 : 한 줄에 20개씩 출력한다.
D=int(input('게임 숫자 입력 : '))
DD=range(1,D+1)

for i in DD:
    if i%10==2 or i%10==4 or i%10==8:
        print('#',end='')
    elif i%20==0:
        print(i)
    else:
        print(i,end='')

print('')
print('----------------------------------------------------------')
# 5
# 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요
# 월(Month)에 해당하지 않는 숫자 입력 시 “잘못된 데이터입니다” 출력
E=int(input('좋아하는 달 입력 : ').strip())
EE=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] # 0번 인덱스에 '0' 값을 주면 -1을 안해도 돼서 편함

if E in [3,4,5]:
    print(f'{EE[E-1]}, Spring')
elif E in [6,7,8]:
    print(f'{EE[E-1]}, Summer')
elif E in [9,10,11]:
    print(f'{EE[E-1]}, Autumn')
elif E in [12,1,2]:
    print(f'{EE[E-1]}, Winter')
else:
    print(f'잘못된 데이터입니다.')


print('----------------------------------------------------------')
# 6
# 숫자와 화폐단위를 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
# 입력은 함수에 넣지 않습니다. 
# 세자리 마다 쉼표(,)와 화폐 단위를 구성해서 출력하는 사용자 정의 함수 생성

def F(num1,str1):
    print(format(num1,',')+str1)
F(5145235,'$')


print('----------------------------------------------------------')
# 7
# 입력받은 정수에 대한 약수를 출력하는 함수를 만들어 주세요
# 약수 = 특정한 수를 다른 수로 나누었을 때, 그 나머지가 0이되는 수
# 형식.join(리스트)를 사용시 리스트 안의 내용들을 형식으로 합쳐줌
def G(num):
    GG=[]
    for i in range(1,num+1):
        if num%i == 0:
            GG.append(str(i))
            GGG=', '.join(GG)
    print(f'{num}의 약수 : {GGG}')

G(72)



print('----------------------------------------------------------')
# 8
# 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.
# 입력 받는 기능은 함수 안에 넣지 않음


def H(msg):
    HH=set()                # set은 저장데이터의 중복을 판별하여 중복값을 제거하여줌
    for num in msg:
        if num.isdigit():
            HH.add(num)
    print(HH)

H('Happy New Year 2023!')



print('----------------------------------------------------------')
# 9
# 생일을 입력 받은 후 한국 나이, 외국 나이를 알려주는 함수를 생성해 주세요. 
# 입력 받는 기능은 함수 안에 넣지 않음
from datetime import datetime           # 현재 날짜를 불러 오기 위해 import로 외부 함수 호출
now=datetime.now()                      # datetime.now() = 현재날짜를 구하기 위한 함수
                                        # .year/.month/.day/.date/.time 등의 기능이 있음

def birth(num):
    age=num.split('.')
    age=list(map(int,age))              # map 함수는 전체 데이터 형식을 바꿔주나 map형식으로 저장되기에 list로 바꾸고 싶다면 꼭 list 씌우기
    if age[1] < now.month:              # 생일 달이 지났을 때
        print(f'당신의 한국 나이는 {now.year-age[0]+1}세입니다. ')
        print(f'당신의 외국 나이는 {now.year-age[0]}세입니다.')
    elif age[1] == now.month:           # 생일 달이 같은 때
        if age[2] <= now.day:           # 생일 달이 같아 day를 비교 지나갔으면 +1 아니면-1
            print(f'당신의 한국 나이는 {now.year-age[0]+1}세입니다. ')
            print(f'당신의 외국 나이는 {now.year-age[0]}세입니다.')
        else:
            print(f'당신의 한국 나이는 {now.year-age[0]+1}세입니다. ')
            print(f'당신의 외국 나이는 {now.year-age[0]-1}세입니다.')             
    else:                               # 생일 달이 지나가지 않았을 때
        print(f'당신의 한국 나이는 {now.year-age[0]+1}세입니다. ')
        print(f'당신의 외국 나이는 {now.year-age[0]-1}세입니다.')
birth('1993.04.02')

print('----------------------------------------------------------')
# 10
# 팩토리얼(Factorial)을 while반복문으로 구현해 주세요. 팩토리얼 수를 입력 받아서 
# 팩토리얼 결과를 아래와 같이 출력하세요
n = int(input('팩토리얼 수 입력 : '))
print(f'{n}! => ', end='')
if (n >= 1):
    fact = 1
else:
    fact = 0
while (n >= 1):
    if (n > 1):
        print(f'{n} * ', end='')
    else:
        print(f'{n} = ', end='')
    fact *= n  #fact=fact*n
    n -= 1     #n=n-1
print(fact)


print('----------------------------------------------------------')
# 11
# 입력받은 숫자 범위 안에서 소수(Prime Number)를 찾아서 반환하는 함수를 생성하세요.
# 입력은 함수에 포함하지 않음
# 소수(Prime Number)란? 1보다 큰 수 중 1과 자기 자신만을 약수로 가지는 수
def primeNumber(num):
    print(f'1 ~ {num} 범위에서의 소수 :',end=' ')
    for i in range(1,num+1):          # i = 1->2->3->4.....->num
        for j in range(2, i+1):       # 위에 for문에서 i값이 고정돼서 들어옴. j = 2->3->4->5.....->i
            if (j == i):              # i=4인체로 내려왔다고 가정해보면
                print(i,end=' ')
            elif (i % j == 0):
                break

primeNumber(30)
print()

print('----------------------------------------------------------')
# 12
# 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수 출력하세요.
# 이름      국어    수학    윤리    국사
# 베트맨    90      89      98      99
# 마징가    82      71      80      91
# 슈퍼맨    77      100     92      90
# 슈렉      94      82      93      71
# 피오나    78      99      91      83
kor={'국어':[90,82,77,94,78]}
math={'수학':[89,71,100,82,99]}
eth={'윤리':[98,80,92,93,91]}
his={'역사':[99,91,90,71,83]}

korjumsu=kor['국어']
mathjumsu=math['수학']
ethjumsu=eth['윤리']
hisjumsu=his['역사']

print(f'[국어] 최고 점수 : {max(korjumsu)}, 최저 점수 : {min(korjumsu)}')
print(f'[수학] 최고 점수 : {max(mathjumsu)}, 최저 점수 : {min(mathjumsu)}')
print(f'[윤리] 최고 점수 : {max(ethjumsu)}, 최저 점수 : {min(ethjumsu)}')
print(f'[역사] 최고 점수 : {max(hisjumsu)}, 최저 점수 : {min(hisjumsu)}')


print('----------------------------------------------------------')
# 13
# 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.
# 입력은 함수에 포함하지 않
# 구구단 출력은 가로(횡) 방향 

def gugudan(start_n,end_n):
    n = start_n
    k = 1
    switch = True
    
    while k != 10:
        if switch:
            print(f"--[{n}단]--",end='     ')
            n +=1
            if n==end_n+1: switch = False; n = start_n; print()

        if not switch:
            print(f"{n}*{k}= {n*k:2}",end='       ')
            n +=1
            if n==end_n+1: n = start_n; k +=1; print()


gugudan(2,4)

# def gugudan(start_n,end_n):
#     n = start_n
#     k = 1
#     switch = True
    
#     while k != 10:
#         if switch:
#             print(f"--[{n}단]--",end='     ')
#             n +=1
#             if n==end_n+1:
#                 switch = False
#                 n = start_n
#                 print()

#         if not switch:
#             print(f"{n}*{k}= {n*k:2}",end='       ')
#             n +=1
#             if n==end_n+1: 
#                 n = start_n 
#                 k +=1 
#                 print()


# gugudan(2,4)

print('----------------------------------------------------------')
# 14
# 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
# 입력은 함수에 포함하지 않음
# 숫자에서 자리 수를 출력하는 기능은 함수로 구현
N = int(input('숫자 입력 : ')) 
 
print(f'만의 자리 : {N % 100000 // 10000}') 
print(f'천의 자리 : {N % 10000 // 1000}') 
print(f'백의 자리 : {N % 1000 // 100}') 
print(f'십의 자리 : {N % 100 // 10}') 
print(f'일의 자리 : {N % 10}')


print('----------------------------------------------------------')
# 15
# 정수, 실수, 논리, 문자열 등 데이터 입력 시 모두 덧셈한 결과 출력하는 함수
# 입력은 함수에 포함하지 않음
# 입력 데이터 수는 미정/가변
# 입력 데이터 종류는 한번에 1개 데이터 타입
# 정수면 정수 데이터만, 문자열이면 문자열 데이터만
def addData(*datas):     
    if len(datas)>0:
        if isinstance(datas[0],str): 
            total='' 
        else:
            total=0
    for data in datas:                              
        total += data                               
    return total


print('----------------------------------------------------------')
# 16
# 아래 출력결과가 나오도록 코드를 작성하세요.
# 크리스마스 트리
for i in range(1,16,2):
    print((" "*((16-1-i)//2)) + ("*"*i))
for j in range(1,3):
    print(" "*(6)+"****")
print(f' Merry Christmas')
print(f'      2023')


print('----------------------------------------------------------')
# 17
# 문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자로 
# 변환하여 출력하는 코드를 구현하세요.
# 리스트 컴프리헨션(List Conprehesion)으로 구현하세요.
msg='Merry Christmas HaPPy New YEaR'
msg=list(msg)
for i in range(0,len(msg)):
    if msg[i].isupper():
        print(msg[i].lower(),end="")
    elif msg[i].islower():
        print(msg[i].upper(),end="")
    else:
        print(msg[i],end="")
print()

newMsg=[msg[i].lower() if msg[i].isupper() else msg[i].upper() if msg[i].islower() else msg[i] for i in range(0,len(msg))]
newMsg="".join(newMsg)
print(newMsg)


print('----------------------------------------------------------')
# 18
# 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후
# 호출하여 결과를 아래와 같이 출력해 주세요.
# 6가지 연산 : 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지값, 몫
def mathematica(num1,num2):
    print(f'덧셈 결과 : {num1+num2}')
    print(f'뺄셈 결과 : {num1-num2}')
    print(f'곱셈 결과 : {num1*num2}')
    if num2==0:
        print(f'나누기 결과 : 0')
        print(f'몫 결과 : 0')
        print(f'나머지 결과 : 0')
    else:
        print(f'나누기 결과 : {num1/num2}')
        print(f'몫 결과 : {num1//num2}')
        print(f'나머지 결과 : {num1%num2}')

mathematica(11,0)


print('----------------------------------------------------------')
# 19
# 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.
# 입력되는 개인정보의 개수는 미정
# 입력하는 사람마다 입력 데이터는 다름
# day1125이론2
def info(**data):
    for key,value in data.items():
        print(f'{key:6} => {value}')
info(age=12,phone='010-1111-2222',job='학생',loc='대구')


print('----------------------------------------------------------')
# 20
# 나의 계산기 프로그램을 구현하세요.

def printMenu():
    print('-'*26)
    print('       <나의계산기>')
    print('-'*26)
    print('       1. 수 입 력')
    print('       2. 덧    셈')
    print('       3. 뺄    셈')
    print('       4. 곱    셈')
    print('       5. 나 눗 셈')
    print('       6. 종    료')
    print('-'*26)


isCheck=False
while True:
    printMenu()
    choice=input('메뉴 선택(1~6): ').strip()
    if choice=='6':
        print('나의 계산기 프로그램을 종료합니다.')
        break
    elif choice=='1':
        nums=input("숫자 2개 입력(ex:3,7) : ").strip()
        num1,num2=nums.split(',')
        num1,num2=int(num1),int(num2)
        print(f'num1 : {num1} / {type(num1)}, num2 : {num2} / {type(num2)}')
        isCheck=True
    elif choice=='2':
        if isCheck:
            print(num1, '+', num2, '=', num1+num2)
        else:
            print('입력된 숫자가 없습니다.')
    elif choice=='3':
        if isCheck:
            print(num1, '-', num2, '=', num1-num2)
        else:
            print('입력된 숫자가 없습니다.')
    elif choice=='4':
        if isCheck:
            print(num1, '*', num2, '=', num1*num2)
        else:
            print('입력된 숫자가 없습니다.')
    elif choice=='5':
        if isCheck:
            print(num1, '/', num2, '=', num1/num2)
        else:
            print('입력된 숫자가 없습니다.') 













