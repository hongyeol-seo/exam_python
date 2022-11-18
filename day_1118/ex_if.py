# ---------------------------------------
# 제어문 : 실행 코드 선택 및 반복 횟수
# - 조건문 : 경우에 따른 실행 여부 결정
# 숫자가 양수인지, 음수인지 검사 후 출력해주세요.
# ---------------------------------------

num = 2
# print(num>0, "양수")
# print(num<0, "음수")

if num>0 : #참이라면 ? True가 된다면 수행가능
    print(f'{num}는 양수입니다.')
else :
    print(f'{num}은 0 또는 음수입니다.')

# if ("1") : 
#     print(1)

# 딕셔너리 안에 키 검사 / 리스트 안에 데이터 인지 검사

jumsu = {'kor':90,'eng':89}

# 딕셔너리 키만 추출
# print(jumsu['ma']) # 이런건 없다

keys = jumsu.keys()

print('mate' in keys) #false 없다 . 내가 찾고자하는 키가 있는지가 

subject = 'kor'

if subject in keys :
    print(f'subject {jumsu[subject]}')

else : 
    print("존재하지 않습니다.")

#[실습]
#데이터를 입력 받고 입력 받은 데이터가 있다면 OK출력
#없다면 데이터 없음 출력

msg = input("데이터를 입력해주세요 : ")

if msg : 
    print("OK")

else :
    print("데이터 없음")

