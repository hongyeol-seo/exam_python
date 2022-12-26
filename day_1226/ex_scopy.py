4# ----------------------------------------------------------------
# 스코프(Scope) : 존재할 수 있는 범위
# ----------------------------------------------------------------

# 전역변수 (Global Variable) : 파일 전체에서 사용되는 변수 / 같은 파일에 존재하는 함수, 클래스, 함께 사용

# 지역변수 (Loval variable) : 특정 영역 안에서만 사용 가능
# 전역 변수와 지역변수의 변수명이 동일한 경우 (백화점에 있는 화장실보다, 집안에 있는 화장실처럼)
# 같은 영역 안에 있는 변수가 우선
# ----------------------------------------------------------------


year = 2022
month = 12

def showToday(day):

    # year += 1 #UnboundLocalError: local variable 'year' referenced before assignment
    # 내 안에 있으면 내꺼부터 쓴다. 그래서 알려줘야한다.
    # 전역변수의 값을 변경한다고한다면

    # 전역변수의 사용을 알려줘야한다.
    global year 
    year += 1 #어떤 year 값을 더해야하는지를 알려줘야한다.
    print(f'오늘은 {year}년 {month}월 {day}일 입니다.')

showToday(26)

print(year)


# 지역변수는 외부에서 사용이 불가합니다.
# print(day)
