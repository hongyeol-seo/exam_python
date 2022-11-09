# ------------------------------------------------
# 숫자 데이터 타입
# ------------------------------------------------
# 다양한 숫자 표현법
bNum = 0b11101 #2진수
oNum = 0o35 #8진수
dNum = 29 #10진수
xNum = 0x1d #16진수

print(f'bNum : {bNum}')
print(f'oNum : {oNum}')
print(f'dNum : {dNum}')
print(f'xNum : {xNum}')

#내가 만약 입력한대로 출력 받고 싶다면?

print(f'bNum : {bNum};{bNum:#b}') #:#b 
print(f'oNum : {oNum};{oNum:#o}')
print(f'dNum : {dNum};{dNum:#d}')
print(f'xNum : {xNum};{xNum:#x}')

# 숫자에 대한 2진수, 8진수, 16진수 값을 알려주는 내장함수
print(31,hex(31),oct(31),bin(31)) 

# ------------------------------------------------
# 산술연산자
num1 = 11 
num2 = 3

print(f'{num1}+{num2} = {num1+num2}')
print(f'{num1}-{num2} = {num1-num2}')
print(f'{num1}*{num2} = {num1*num2}')
print(f'{num1}/{num2} = {num1/num2}')
print(f'{num1}//{num2} = {num1//num2}') #몫
print(f'{num1}**{num2} = {num1**num2}') #제곱

# >>> 터미널에 이렇게 나온다는 것은 바로 바로 확인을 하겠다는 의미

#----------------------------------------------------------------
# 비교연산자 

num1 = 11 
num2 = 3

print(f'{num1}>{num2} = {num1>num2}')
print(f'{num1}<{num2} = {num1<num2}')
print(f'{num1}>={num2} = {num1>=num2}')
print(f'{num1}<={num2} = {num1<=num2}')
print(f'{num1}=={num2} = {num1==num2}')
print(f'{num1}!={num2} = {num1!=num2}')

#----------------------------------------------------------------
# 논리연산자

num1 = 11 
num2 = 3

print(f'{num1}>{num2} and {num1} == {num2} : {(num1>num2) and (num1 == num2)}')
print(f'{num1}<{num2} and {num1} == {num2} : {(num1<num2) and (num1 == num2)}')
print(f'{num1}>{num2} and {num1} >= {num2} : {(num1>num2) and (num1 >= num2)}')

num1 = 11 
num2 = 3

print(f'{num1}>{num2} or {num1} == {num2} : {(num1>num2) or (num1 == num2)}')
print(f'{num1}<{num2} or {num1} == {num2} : {(num1<num2) or (num1 == num2)}')
print(f'{num1}>{num2} or {num1} >= {num2} : {(num1>num2) or (num1 >= num2)}')

num1 = 11 
num2 = 3

print(f'{num1}>{num2} or {num1} == {num2} : {not num1>num2}')
print(f'{num1}<{num2} or {num1} == {num2} : {not num1==num2}')

#객체 비교

a = 10
b = 9
b += 1

print(id(a), id(b))
 
num1 ="가"
num2 ="가"

print(f'id(num1) : {id(num2)}, id(num2) : {id(num2)}')
print(f'{num1} is {num2}:{num1 is num2}')
print(f'{num1} == {num2}:{num1 == num2}') #산술연산자의 경우에는 값을 비교

num1 =10
num2 =num1

print(f'id(num1) : {id(num2)}, id(num2) : {id(num2)}')
print(f'{num1} is {num2}:{num1 is num2}')
print(f'{num1} == {num2}:{num1 == num2}') #산술연산자의 경우에는 값을 비교

#-------------------------------------------------------------
# 형변환 Type Casting
# - 자료형 즉 Data type을 변경시키는 것
# - 데이터 손실 발생 가능
# - 내장 함수

avg = 89.23
print(f'{avg} => {type(avg)}')
print(f'{int(avg)} => {type(int(avg))}')
print(f'{avg} => {type(avg)}') #영구적으로 바뀌는 것이 아니다. #바꾼걸 저장해야지만 형변환이 일어난다.

