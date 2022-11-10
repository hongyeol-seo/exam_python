# 1. 자료형(데이터 타입)에 대해 간단하게 설명해 주세요.

# 데이터를 저장하기 위한 데이터 종류를 말하며 \n 
# 정수를 저장하는 int 타입,실수를 저장하는 float 타입, \n
# 복소수를 저장하는 complex 타입 그리고 문자형을 저장하는 str 타입과 \n
# 논리형으로 bool 타입이 있으며, 0 ~ 255 사이의 코드를 저장하는 bytes 자료형이 있습니다. \n

# 데이터를 메모리에 저장하기 위한 데이터의 종류를 말하며, 저장될 수 있는 범위가 다르다.

# 2. 파이썬에서 자료형 종류별 예시 및 타입을 출력하는 코드를 작성하세요.

print(f'int 형 : type(4) = {type(4)}')
print(f'flat 형 : type(3.14) = {type(3.14)}')
print(f'complex 형 : type(1+2j) = {type(1+2j)}')
print(f'str 형 : type("홍열") = {type("홍열")}')
print(f'bool 형 : type(True) = {type(True)}')

# 3. 정수 31을 2진수, 8진수, 10진수, 16진수로 출력하세요.

print(f'31, 2진수 {bin(31)}, 8진수 {oct(31)} 16진수 {hex(31)} ')

# 4. 자료형(데이터 타입)을 변경하는 것을 (형변환 )이라 합니다.

average=98.7
print(f'98.7 정수로 변환 {int(average)}')

year=2022
print(f'2022 실수로 변환 {float(year)}')


# 5. 2개 정수를 입력 받아서 산술연산, 비교연산, 논리연산 수행 결과를 출력하는 코드를 작성하세요.

#산술연산

a = int(input("정수를 입력하세요 : "))
b = int(input("정수를 입력하세요 : "))

print(f'{a}+{b} = {a+b}')
print(f'{a}-{b} = {a-b}')
print(f'{a}*{b} = {a*b}')
print(f'{a}/{b} = {a/b}')
print(f'{a}//{b} = {a//b}') #몫
print(f'{a}**{b} = {a**b}') #제곱

#비교연산 

print(f'{a}>{b} = {a>b}')
print(f'{a}<{b} = {a<b}')
print(f'{a}>={b} = {a>=b}')
print(f'{a}<={b} = {a<=b}')
print(f'{a}=={b} = {a==b}')
print(f'{a}!={b} = {a!=b}')

#논리연산 

print(f'{a}>{b} and {a} == {b} : {(a>b) and (a == b)}')
print(f'{a}<{b} and {a} == {b} : {(a<b) and (a == b)}')
print(f'{a}>{b} and {a} >= {b} : {(a>b) and (a >= b)}')

print(f'{a}>{b} or {a} == {b} : {(a>b) or (a == b)}')
print(f'{a}<{b} or {a} == {b} : {(a<b) or (a == b)}')
print(f'{a}>{b} or {a} >= {b} : {(a>b) or (a >= b)}')

print(f'not a>b : {not a>b}')
print(f'not a==b : {not a==b}')