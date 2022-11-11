# --------------------------------
# 메서드 (Method)
# - 특정 클레스에서만 사용되는 함수를 말함
# - 사용 : 객체 생성 후 사용 가능
# - 예시 ) name = "Hong"
#          name.메서드명()
#          name.속성명()

msg = "Merri Chrstmas!"

# "i" => "Y"
# 인덱스로 변경하는 방법
# msg[4] = "y" # not support item assignment 인덱스로 제공하는 것 불가능
# print(msg)

# 방법 2번 str타입의 전용 메서드 replace()
print(msg.replace("r","y")) #첫번째, 두번째 / unexpected EOF while parsing / 이거 속성값도있던데? / 몇 개를 바꿀 수 있는가? default 값으면 -1인데 이건 다 바꾸라는 말
# replace(바꿀문자열, 새로운문자열)

# 문자열에서 인덱스를 찾아주는 메서드
# find(문자열) => 양수인덱스 / 없는 경우 -1
# index(문자열) => 양수인덱스 / 없는 경우 : Error

print(f'{msg} => C 인덱스 : {msg.find("C")}')
print(f'{msg} => mas 인덱스 : {msg.index("mas")}') #여러개 문자가 모인경우에는 문자가 시작되는 인덱스를 준다

#특정 문자가 여러개 존재하는 경우/ 

print(f'{msg} => C Find : {msg.find("r")}') #제일 먼저 발견되는 문자열. 만약에 문자열의 뒤에서부터 찾는 경우에는 rfind!
print(f'{msg} => C Find : {msg.rfind("r")}') #만약에 문자열의 뒤에서부터 찾는 경우에는 rfind! reverse! 

#인덱스 메서드로 찾기.

print(f'{msg} => C 인덱스 : {msg.index("r",4)}') #없을때는 오류를 보낸다.  #옵션값으로 뒤에 주고 있
#파인드를 쓸지, 인덱스를 쓸지! 

#__ 언더바가 붙어있는 속성이나 함수들은 스페셜 기능! 클래스 만들때 쓴다.

#문자열에서 특정 문자열이 몇 개 있는지 알려주는 메서드! => count()
data = "Happy Happy"
pCount = data.count('p') 

#data 문자열에서 'p'가 존재하는 갯수만큼 data를 화면에 출력해주세요.

print(data * data.count('p'))

#소문자를 대문자로
#대문자를 소문자로
print(data.upper())
print(data.lower())

data1 ="     happy happy     "

# 공백제거하는 메서드
# 내장함수 len(변수명) => 갯수/길이를 반환

print(f'{data1} 길이 : {len(data1)}')

data2 = data1.strip()
print(f'{data2} 길이 : {len(data2)}')

data3 = data1.rstrip()
print(f'{data3} 길이 : {len(data3)}')

data4 = data1.lstrip()
print(f'{data4} 길이 : {len(data4)}')

# print(data.strip()) #앞/뒤 공백제거
# print(data.lstrip()) #앞 공백제거
# print(data.rstrip()) #뒤 공백제거

#문자열 나누기! #특정 문자열을 기준으로 나누기! split() 공백을 기준으로 문자열을 나눕니다.

data = "Happy New Year 2023"
#기본 - 공백으로 나누기
datas = data.split()
print(datas)

data = data.replace(" ","*") #빈공간을 별로 바꾸기!
print(data)

#아스타리크로 문자열 나누기 
print(data.split("*"))

pNumber = "010-8583-8748"
print(pNumber.split("-"))

#여러개의 문자열을 연결 또는 삽입 메서드 #join 메서드
#형식 : 연결할 문자열.join(여러개 문자열)

phone = "010-8583-8748"
phone2 = phone.split('-')
print(f"phone2 : {phone2}")
# print('.'.join(phone2))
new_phone = '.'.join(phone2)
print(f'new phone : {new_phone}')
new_phone = ' '.join(phone2)
print(f'new phone : {new_phone}')

# [실습]
# 하고 싶은 말을 입력받아서, 출력하기
talk = input("하고 싶은 말 입력 : ")
print(type(talk)) 
print(f'talk 길이 : {len(talk)}') #공백제거

talk = talk.strip()
print(f'talk 길이 : {len(talk)}') #공백제거

