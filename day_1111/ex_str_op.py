# ---------------------------------------------------
# 문자열 str 타입 연산 수행
# ---------------------------------------------------

name = "Hong"
gender = "M"

# 산술연산 수행 -------------------------------------
# 덧셈 : str + str = 문자열 연결
print(f"{name} + {gender} = {name+gender}")
# print(f"{name} + {2022} = {name+2022}") #문자열끼리만 덧셈 가능
# 오직 str + int 안됨! 오직 str + str만 됨
print(f"{name} + {str(2022)} = {name+str(2022)}")
1
#뺄셈 : str - str = 지원되지 않는 기능
# print(f"{name} - {gender} = {name-gender}") #unsupported operand 이 연산 기능을 지원하지 않는다.

#곱셉
# print(f"{name} * {gender} = {name*gender}") #can't multiply sequence #곱하기는 int랑만 가능!
print(f'{name} * 5 = {name * 5}') #5번 반복!

# 나머지(%) => d는 정수, f는 실수, s는 문자열 

#[실습] --------------------------------------------
# 출력 => =====================================
#                    My Program
#         =====================================

print("\t\t\t\t"+"="*25)
print(f'\t\t\t\t\tMy Program')
print("\t\t\t\t"+"="*25)

#한 줄로 만들기!

print("="*25 + '\n\tMy Program\n' + "="*25)

# 멤버 연산자 -------------------------------------
# 요소 in 그룹 : 요소가 그룹에 존재 하면 True
# 요소 not in 그룹 : 요소가 그룹에 존재하지 않으면 True

data = "Good"
print(f'G in {data} : {"G" in data}')
print(f'g in {data} : {"g" in data}') #대,소문자를 구별한다.
print(f'oD in {data} : {"oD" in data}') #아스키 키보드표를 보면, 다르다.
print(f'oD not in {data} : {"oD" not in data}') #아스키 키보드표를 보면, 다르다.

# 문자열 처리 함수들 -> 메서드
# class str, class int 
# 클래스가 객체가 되어야만 사용할 수 있다.
# 'happy'.encode 이런 애들도 가능하다
# (1). 숫자는 그렇게한다.
