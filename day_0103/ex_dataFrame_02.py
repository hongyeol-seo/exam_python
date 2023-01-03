import pandas as pd

data = [[10,20,30],["F",'M',"N"],[11,22,33],[44,55,66],['A','B','C']]

df1 = pd.DataFrame(data)

# DF 요소/원소 다루기 -------------------
# 열(컬림) 기준으로 요소
# 0번 컬럼 가져오기 => 변수명[컬럼]

print(f'컬럼명 => {df1.columns}')
one = df1[0]
print(f'타입 {type(one)}\n{one}')

print("===================")
for col in df1.columns:
    print(f'타입 {type(df1[col])}\n{df1[col]}')

# 여러개 컬럼(열) 요소 가져오기 0번이랑 2번 가져오기
# 2개 이상을 가져올때는 데이터 프레임
print(f'여러개 가져오기\n {df1[[0,2]]}')

#슬라이싱
#컬럼이 아니라, 로우가 나온다.
#데이터 프레임에서 슬라이싱을 가져오면, 컬럼에 슬라이싱을해서는 원한는 값을 뭔가져온다.
#범위지정데이터 추출이 안된다.
print(f'슬라이싱 가져오기\n{df1[0:2]}') 

# =======================================
# D/F 요소/원소 다루기 열(coslums)
# 데이터프레임의 컬럼 속성 변경 ==> 변수명.속성명, 새로운 값

df1.columns=["one","two","three"]
print(f'변경확인 {df1.columns}') #속성을 읽을 수도 있지만, 변경할 수도 있다.

print(f'df1["one"] =>\n{df1["one"]}\n{type(df1["one"])}')
print(f'df1.one =>\n{type(df1.one)}') #변수명[컬럼] or 변수명.컬러명
# print(f'df1.one =>\n{type(df1[0])}') 
# #변수명[컬럼] or 변수명.컬러명
# 단, 컬럼이 문자열 str인 경우 #KeyError:  #컬럼은 원래 안주면 0,1,2
# 기존에 있었던 0,1,2를 쓸 수 없음. 시리즈에서는 같이 사용이 되었는데, 
# 판다스 df에서는 사용 불가 
# 단, 1개 컬러만 가능

# D/F 요소/원소 다루기 행(row)
# 변수명.iloc[인덱스] : 반드시 정수형 인덱스만 가능 itiger
# 변수명.loc[인덱스] : 문자열 인덱스
# 0번 행 데이터 가져오기
zeroRow = df1.iloc[0]
print(f'zeroRow[]=>\n{zeroRow}\n{type(zeroRow)}') #한줄 가져오기 때문에 시리즈
#가로든 세로운 한 줄을 가져오면

#2개 행 데이터 가져오기
#변수명.iloc[[인덱스, 인덱스]]
zeroTwoRow = df1.iloc[[0,1]]
print(f'zeroTwoRow[]=>\n{zeroTwoRow}\n{type(zeroTwoRow)}')

#범위지정 => 슬라이싱 변수명.iloc[시작:끝+1] olr 변수명[시작:끝+1]

oneThree = df1.iloc[1:4]
print(f'oneThree[]=>\n{oneThree}\n{type(oneThree)}')

oneThree2 = df1[1:4] #컬럼이 아니라, 로우를 가져온다. / 
print(f'oneThree[]=>\n{oneThree}\n{type(oneThree)}')

#행(row) 인덱스 속성 변경 후 행 추출 -------------------------------
df1.index=["A","B","C","D","E"]
print(f'행인덱스 변경후\n{df1}')

# zeroRow = df1.iloc["A"] #Cannot index by location index with a non-integer key
zeroRow = df1.loc["A"]
zeroRow = df1.iloc[0] #행인덱스는 살아있다.
# zeroRow = df1.loc[0] i가 붙어있으면 정수가 쓰여져있어야한다.

# T 트렌스!

# Q. 열인덱스의 이름의 속성값을 변경하면 사라진다?
# Q. 리스트 슬라이싱 할 때, 끝자리가 포함되어있는것은 뭐였지?

#원소/요소 (element) 추출하기
print(f'-------------------------------------')
print(df1)

#사용법 : 변수명.iloc[행인덱스, 열인덱스], 변수명.iloc[행인덱][열인데긋]
#사용법 : 변수명.loc[행인데긋,열인덱스],변수명.loc[행인덱스][열인덱스]

v33 = df1.loc["C","three"]
v22 = df1.loc["C"]["three"]

print(f'{v33}, {v22}')
#데이터 44, 66 추출

v4466 = df1.loc["D",['one','three']]
print(f'{v4466},{type(v4466)}')
vv=df1.iloc[[0,2],[1,2]] #번호로 바꾸었지만 #loc는 죽었지만, iloc는 살이있네
#요소값이 20,30, 22, 33인데이터 출력
v = df1.loc[['A','C'],['two','three']]

print(v)
print(vv)
#곱셉이 들어가네?

#데이터 프레임 삭제
# axis = 0 기본값 횡 / 횡은 레코드 / 관측값 