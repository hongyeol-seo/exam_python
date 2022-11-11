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
print(msg.replace("r","y")) #첫번째, 두번째 / unexpected EOF while parsing / 이거 속성값도있던데?
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

print(f'{msg} => C 인덱스 : {msg.index("r",4)}') #없을때는 오류를 보낸다. 
#파인드를 쓸지, 인덱스를 쓸지! 
