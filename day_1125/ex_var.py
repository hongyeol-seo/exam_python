# 스코프
# 변수의 사용 가능한 범위&

year= 2022

for _ in range(10):
    total = 10

if False :
    msg = "Good Luck"


# print(year,total,msg) #name 'msg' is not defined
# 전역변수 global variable 파이썬 파일 안에 모든 곳에서 사용 가능한 변수
#  

year = 2022
msg = 'None'
# 함수에서 사용되는 변수 -> 매개변수, 함수 내부의 변수
# 함수에만 사용되는 변수 -> 지역변수
# 매개변수 month

def addYear(month):
    global year
    year = year+1 #local variable 'year' referenced before assignment 
    #값을 바꿀려고하는데, 공용화장실바꾸려고한다면, 알려줘야한다. 내가 global year를 사용할께
    msg = 'Happy'
    print(year+10, month,msg)
    #함수의 변수는 할일 다 하고 나면 사라진다.

for _ in range(0):
    total = 10

if True :
    msg ="Good Luck"

print(f'before : {year}')
addYear(12)
#함수에 포함된 지역변수는 함수 밖에서 사용불가!
# print(year,month)

print(f'after : {year}') #변경! 
