# ➀ “Happy New Year 2022” 문자열에서 2022를 2023으로 변경해 주세요.


strMsg = "Happy New Year 2022"
strMsg3 = strMsg[:-1] + strMsg[-1:].replace("2","3")
print(f"변경된 문자열 : {strMsg3}")

# ➁ “christmas” 문자열을 모두 대문자로 변경해 주세요.

strUpper = "christmas"
strUpper = strUpper.upper()
print(f"변경된 문자열 : {strUpper}")

# ➂ phone_number = "010-1111-2222" 문자열을 “01011112222”로 출력해 주세요. 

phone_number = "010-1111-2222"
phone_number = phone_number.replace("-","")
print(f'변경된 문자열 : {phone_number}')

# ④ count = "5,969,782,550" 문자열에서 콤마(,)를 제거하고 정수로 출력해 주세요. 

count = "5,969,782,550"
count = int(count.replace(",",""))
print(f'변경된 문자열 : {count}')

# ⑤ “산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐”에서 “어디를”이 몇 개 있는지 출력해주세요. 

countMsg = "산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐"
print(f"\'어디를\'이 몇 개 있는가? : {countMsg.count('어디를')}")

# ⑥ “1,234,567,890” 문자열을 나누어 주세요.

strSplit = "1,234,567,890"
strSplit.split(",")

print(f'\'.\'를 기준으로 문자열 나누기 : {strSplit.split(",")}')

# ⑦ “koko@naver.com”에서 ”@“의 인덱스를 출력해 주세요. 

strIndex = "koko@naver.com"
strIndex = strIndex.index("@")
print(f'“koko@naver.com”에서 ”@“의 인덱스를 출력 : {strIndex}')

# ⑧ “ 오늘은 날씨가 너무 좋군요!! ”에서 공백을 제외한 문자의 길이를 출력해 주세요.

strLen = ' 오늘은 날씨가 너무 좋군요!! '
strLen = strLen.strip().replace(" ","") #양쪽공백과 띄어쓰기 제거
print(f'공백을 제외한 문자의 길이 : {len(strLen)}')

# 2. [문자열] 아래 출력결과가 나오도록 코드를 작성하세요.
for i in range(1,17,2) :
    print("{0:^15}".format("*" * i))

print("{0:^15}".format("*" * 4))
print("{0:^15}".format("*" * 4))
print("{0:^15}".format("Merry Christmas"))
print("{0:^15}".format("2023"))

# 3. 아래 조건에 맞도록 코드를 작성하세요.
# ➀ 숫자 2개를 입력 받은 후 산술연산 수행 후 출력해 주세요. 덧셈, 뺄셈, 곱셈, 나눗셈

intX = float(input("첫 번째 숫자를 입력해주세요 : "))
intY = float(input("두 번째 숫자를 입력해주세요 : "))
print(f'intX + intY = : {intX+intY}')
print(f'intX - intY = : {intX-intY}')
print(f'intX * intY = : {intX*intY}')
print(f'intX / intY = : {intX/intY}')

# ➁ 좋아하는 단어를 입력 받은 후 대문자로 변환하여 출력하세요.
# 그리고 단어 안에 ‘a’ 알파벳이 들어 있는지 True 또는 False로 결과를 출력해주세요.
strInput = input("단어를 입력하세요 : ")
strInput1 = strInput.upper()
print(strInput1)
print("a" in strInput)

# ➂ “Hello”를 거꾸로 “olleH” 출력하세요.

strReverse = "Hello"
print(strReverse[::-1])