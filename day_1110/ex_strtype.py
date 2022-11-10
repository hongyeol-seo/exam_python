# 문자 데이터 -> str 타입 자료형
# '문자', "문자", '''문자''', """문자""" #주석이 아니라 str 저장할때는 주석이 아니다. 다른 언어랑 달리, 파이썬은 모든 문자형 자료형을 str로 본다.

name = '마징가'
name = "'마징가'"
name = """Maginga"""
name = '''Maginga'''
korea = "대한민국"
print(f'name : {name}')

# ------------------------------------------------
# str에서 문자 1개만 출력하기
# 인덱싱 (Indexing) 
# M a g i n g a
# 0 1 2 3 4 5 6
# 뒤에서부터는 -1
# 변수명에[인덱스]
# ------------------------------------------------

print(name[0:3])
print(korea[-1])

# 실습 : Good Luck ~! 

message = "Good Luck~!"

print(message[5:7])
print(message[5:])
print(message[:7])
print(message[-3:])

# ------------------------------------------------------
# 슬라이싱
# => 문자열에서 구간(범위) 정해서 일부 문자열 잘라내기!
# => 변수명[시작인덱스:끝인덱스]

# [실습] "Merry Christmas~ 2022 12 24^^"
# (1)년월일만 출력하기
# (2)Chirstmas~ 출력
# (3)년월일에 ^^표시까지 출력하기

text = 'Merry Christmas~ 2022 12 24^^'

print(len(text))

print(text[17:27])
print(text[6:15])
print(text[17:])

print(text[0:5])

# 규칙
# strNumber / 변수명 짓는 규칙 / strAge / 변수의종류까지 알 수 있또록
# strNumber 아! 문자열이 있겠구나!

strNumber = "CODE_123456789"

# 13579 만출력
print(strNumber[5],strNumber[7],strNumber[9],strNumber[11],strNumber[13])

# 연속되지는 않았지만, 빼오는 규칙이 있다. 두 칸씩있기 때문에 이걸 가지고 슬라이싱을 하면 된다.
# 변수명[시작인덱스:끝인덱스+1:규칙/간격]

print(strNumber[5:14:2]) #끝규칙
print(strNumber[5::2]) #끝은 생략 그 대신, 2씩 증가

#[실습] ----------------------------------------
# 본인의 생년월일 계절을 한번에 입력 받아서 년, 월, 일 계절을 네 개의 변수에 저장하기

birthmessage = input("본인의 생년월일과 계절을 입력해주세요 ex) 1992년4월13일warm : ")
# 입력 받은 데이터를 확인하고
print(f'Mybirth 타입 : {type(birthmessage)}')

# 각 변수에 할당해서
year = birthmessage[:5]
month = birthmessage[5:7]
day = birthmessage[7:10]
season = birthmessage[10:]

print(year, month, day, season)