#115

num = int(input("정수를 입력해주세요. : "))

num1 = (num-20)

if num1 < 0 :
    print(0)

elif num1 > 255 :
    print(255)

#116
time = input(" 현재시간: ").strip()
newtime = int(time[-2:])

if newtime == 00 :
    print("정각입니다.")

else :
    print("정각이 아닙니다.")

#117
fruit = ["사과", "포도", "홍시"]
# msg = input("좋아하는 과일은? : ")

if "사과" in fruit :
    print("정답입니다.")

else :
    print("오답입니다.")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

msg = "봄"
if msg in fruit.keys() :
    print("정답입니다.")

else:
    print("오답입니다.")

# fruit.get(msg,"오답입니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

msg = "한라봉"

print(fruit.get(msg,"오답입니다."))

#123

won = {"달러":1167,"엔":1.096,"유로":1268,"위안":171}

msg = "100 달러"

msg = msg.split(" ")

print("{:.2f} 원".format(int(msg[0])*won[msg[1]]
))

# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

#125
번호 = {"011":"SKT","016":"KT","019":"LGU","010":"알수없음"}

num = '011-345-1922'
print("당신은 %s 사용자입니다."%(번호.get(num[:3])
))

#126
우편번호 = "01400"
i = int(우편번호[2])
print(i)
if i in [0,1,2,]:
    print('강북구')
elif i in [3,4,5]:
    print("도봉구")

#128 ★
주민등록번호 =  "861010-1015210"
뒷번호 = 주민등록번호.split("-")[1]

if int(뒷번호[2]) > 9 or int(뒷번호[1:3]) > 10 :
    print("서울사람이 아닙니다.")

elif int(뒷번호[2]) <= 8 :
    print("서울사람입니다.")

주민번호 = "861010-1015210"
뒷자리 = 주민번호.split("-")[1]
print(int(뒷자리[1:3]))

str = "08"
print(int(str))

#129 ??? 일일히 다 대입해서 푸는문제야?
num = "920413-1008910"
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

#130 get!?
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(btc)