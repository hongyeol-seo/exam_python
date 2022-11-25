# 1. fruits = ["사과", "귤", "수박"]에서 요소를 하나씩 모두 출력하세요.

fruits = ["사과", "귤", "수박"]

for idx in fruits:
    print(idx)

# 2. 1~50 범위에서 3의 배수와 7의 배수로 데이터를 저장한 후 모든 요소를 내림차순 으로 출력해주세요.

s1 = list(range(3,51,3))
s2 = list(range(7,51,7))
s3 = sorted(s1 + s2,reverse=True)

for idx in range(len(s3)):
    if not idx%5 :
        print(s1[idx],end="\n")
    print(s1[idx],end="\t")
    

# 3. dataEng=[‘Happy’, ‘Good’, ‘Dog’, ‘Cat’] 모든 요소를 소문자로 출력하세요.

data=["Happy","Good","Dog","Cat"]

for idx in range(len(data)):
    data[idx] = data[idx].lower()

print(f"소문자 출력 {data}")


# 4. com = ["SK하이닉스", "삼성전자", "LG전자"]에서 모든 요소와 길이를 출력하세요.

com = ["SK하이닉스", "삼성전자", "LG전자"]

for idx in range(len(com)) :
    print(f'{com[idx]}의 길이 : {len(com[idx])}')


# 5. numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23]에서 짝수번째 요소만 모두 더한 결과를 출력하세요.

numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23]

sum = 0

for idx in range(len(numList)) :
    if not idx%2 :
        sum += numList[idx]

print(f'합계 : {sum}')

# 6. 사용자로부터 원하는 단을 입력 받아서 해당 구구단을 출력하세요. 

dan = input("단을 입력해주세요. : ").strip()

if len(dan) > 0 and dan.isdecimal() :
    #null여부 & #숫자여부체크
    dan = int(dan)
    for idx in range(1,10):
        print(f"{dan} + {idx} = {dan*idx}")

else :
    print("입력값 오류")

# 7. OHLC=[["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190],
#  [300, 310, 300, 310]]에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가
#  3일치 날짜별로 저장되어 있습니다.
#  시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하여 이익("gain")
#  데이터 추가하세요. 그리고 3일치 종가와 이익을 출력해 주세요.

OHLC=[["open", "high", "low", "close"],[100, 110, 70, 100], [200, 210, 180, 190],[300, 310, 300, 310]]

benefit = 0 

for idx in range(1,4):
    print(f"{idx}일째 종가 : {OHLC[idx][3]}")
    print(f"{idx}일째 수익 : {OHLC[idx][3] - OHLC[idx][0]}")
    benefit += (OHLC[idx][3] - OHLC[idx][0]) 
    
print(f'수익금 {benefit}')

# for item in OHLC[1:]:
# item.append(item[-1]-item[0])
# print(f'종가 : {item[-2]} 이익 : {item[-1]:3}')

# 8. 현재 시간을 입력 받은 후 아래와 같이 출력하세요. 예) 13:00 => 정각 오후 01시 정각입니다. 12:00 => 정오 12시 정각입니다.
#  3:21 => 오후 01시 21분입니다. 09:08 => 오전 09시 08분입니다.
intputStr = "12:00"

h = intputStr[:2]
m = intputStr[-2:]

if h == "00" :
    #자정
    if m == "00" :
        print(f"자정 {h}시입니다.")
    else :
        print(f"오전 {h}시{m}분입니다.")
    
elif 12 > int(h) > 0 :
    #오전
    if m == "00" :
        print(f"오전 정각 {h}시입니다.")
    else :
        print(f"오전 {h}시 {m}분입니다.")

elif h == "12" :
    #정오
    if m == "00" :
       print(f"정오 {h}시입니다.")
    else :
        print(f"오후 {h}시{m}분입니다.")
else :
    #오후
    if m == "00" :
        print(f"오후 정각 {h}시입니다.")
    else :
        print(f"오후 {h}시 {m}분입니다.")


# 9. 우편번호는 5자리로 구성되며, 앞의 세 자리수로 구를 판별할 수 있습니다.
#  강북구, 도봉구, 노원구의 우편번호는 01로 시작하고 세 번째 자리 숫자로 구를
#  구분합니다. 강북구 => 010, 011, 012, 도봉구 => 013, 014, 015, 노원구 =>
#  016, 017, 018, 019입니다. 5자리 우편번호 입력받아 지역구 판별하여 출력하세요. 

우편번호 = "01400"
i = int(우편번호[2])
print(i)
if i in [0,1,2,]:
    print('강북구')
elif i in [3,4,5]:
    print("도봉구")
elif i in [6,7,8]:
    print("노원구")

# 10. 구구단을 아래 처럼 되도록 출력하세요. --[2]-- --[3]-- --[4]-- --[5]-- --[6]-- --[7]-- --[8]-- --[9]--
#  2*1= 2 3*1= 3 4*1= 4 5*1= 5 6*1= 6 7*1= 7 8*1= 8 9*1= 9
#  2*2= 4 3*2= 6 4*2= 8 5*2=10 6*2=12 7*2=14 8*2=16 9*2=18
#  : : : : : : : :
#  2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81

print("--[2]-- --[3]-- --[4]-- --[5]-- --[6]-- --[7]-- --[8]-- --[9]--")
for i in range(1,10):

    for j in range(2,10) :
        print(f'{j}*{i}={j*i}',end="\t")
    
    print("")

# 11. 아래 그림처럼 나오도록 코드 작성하세요. 가장 긴 라인의 별의 수는 15개,
#  전체 라인수도 15라인 입니다.

for i in range(8):
    print("{:^15}".format("*"*(2*i+1)))
for i in range(7):
    print("{:^15}".format("*"*(13-2*i)))


