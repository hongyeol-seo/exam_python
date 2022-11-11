# 1. [변수] 데이터를 저장하는 코드를 작성해 주세요.

# ➀ 자신의 고향 도시를 저장하세요.
strCity = "Seoul"
# ➁ 자신의 혈액형을 저장하세요.66 
strBlood = "A"
# ➂ 좋아하는 계절을 저장하세요. 
strSeason = "Warm"
# ④ 키를 저장하세요.
numHeight = 185 
# ⑤ 전화번호를 저장하세요
strNumber = "010-8583-8748" 
# ⑥ 파이(π)값을 저장하세요.
numPi = 3.14 
# ⑦ 국적을 저장하세요
strNation = "Korea"

# 2. [입력함수 & 형변환] 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.

# 예) [입력] 궁금한 구구단 : 5 ↲
# [출력] 
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 20
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45

intGugudan = int(input("궁금한 구구단 : "))
for i in range(10):
    print(f'{intGugudan} * {i} = {intGugudan*i}')


# 3. [자료형변환] 아래 조건에 맞도록 코드를 작성하세요
# ➀ 정수 31 ==> 실수로 일시적 변환

a = 31 
print(type(float(a)))
print(type(a))

# ➁ 정수 31 ==> 실수로 완전히 변환
a = 31 
print(type(a))
a = float(a)
print(type(a))

# ➂ 정수 2022 ==>문자열로 일시적 변환
a = 2022
print(type(str(a)))
print(type(a))

# ④ 정수 2022 ==>문자열로 완전히 변환

a = 2022
print(type(a))
a = str(a)
print(type(a))

# ⑤ 실수 98.1 ==> 정수로 일시적 변환

a = 98.1
print(type(a))
print(type(int(a)))
print(type(a))

# ⑥ 실수 98.1 ==> 정수로 완전치 변환
a = 98.1
print(type(a))
a = int(a)
print(type(a))

# ⑦ 실수 98.1 ==> 문자열로 일시적 변환
a = 98.1
print(type(str(a)))
print(type(a))

# ⑧ 실수 98.1 ==> 문자열로 완전히 변환
a = 98.1
a = str(a)
print(type(a))


# 4. 아래 데이터를 출력하도록 코드를 작성하세요.

# ➀ 주민등록번호는 881120-1068234입니다.
# 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로
# 나누어 출력하세요.

intZuminNumber = "881120-1068234"
print(intZuminNumber[0:6])
print(intZuminNumber[7:])

# ➁ 문자열 a:b:c:d가 있습니다.
# 해당 문자열에서 a, b, c, d 만 출력해 주세요.

strX = "a:b:c:d"
print(strX[0],strX[2],strX[4],strX[6])
print(strX[0::2])

# ➂ 문자열 “AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr“에서
# [ 출력 ]
# 대문자만 출력 : ABCDEFGHIJKLMNOPQR
# 소문자만 출력 : abcdefghijklmnopqr

strABC = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(strABC[0::2])
print(strABC[1::2])

#④ 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서
#판매되고 있습니다. 총 금액을 출력해 주세요.

intSum = 48584
intMonth = 38
print(f'총금액 : {intMonth * intSum}')

#⑤ “가로 10cm, 세로 11cm인 직사각형 넓이 계산” 문자열로
#구한 값으로 직사각형 넓이 계산 후 출력하세요.
#[ 출력 ]
#직사각형 넓이 : 가로 10 x 세로 11 = 110

strText = "가로 10cm, 세로 11cm인 직사각형 넓이 계산"
print(strText[3:5])
print(strText[12:14])

intX = int(strText[3:5])
intY = int(strText[12:14])

print(f'직사각형 넓이 : 가로 10 x 세로 11 = {intX * intY}')