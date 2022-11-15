# ------------------------------------------
# 함수(function) vs 메서드(method)
# - 공통점 : 형태 동일
# - 차이점 : 이름이 다름, 사용범위
# 누구나 사용 가능 -> 함수 
# 특정 데이터 타입만 사용 가능 -> 메서드
# ★특정 데이터 타입 객체변수명.메서드() .format
# -------------------------------------------
# str 데이터 타입 전용 함수. 즉 메서드 -----------------
msg = 'good lucck'
print(msg.upper(),msg)

#이전문자 -> 새로운 문자 변경 메서드 
print(msg.replace("cc","c"))

#문자열을 특정 기준으로 문자열 나누기 split()
print(msg.split())

#재미잇는 str메서드 -------------------------------------
#첫 번째 문자열 체크 후 결과를 true or false 내놔라

print(msg.startswith("Go"))

#문자열 끝부분을 체크 후 결과 True/False => endswith()
print(msg.endswith("ck"))

#입력 받은 데이터가 숫자, 문자인지 검사 후 결과 true/false

msg = "123213"
msg2 = "Asdfasdfadf"

print(msg, msg.isnumeric()) #문자열이 숫자로 이루어져있는지, 아닌지
print(msg, msg2.isalpha()) #문자열이 영어로 이루어져있는지, 아닌지
