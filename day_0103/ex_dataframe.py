import pandas as pd
# --------------------------------
# 데이터 프레임
# ----------------------------------
# 판다스의 구조형 데이터 타입
# 구성 : 열과 행
# 행인덱스, 열인덱스

# 데이터 => list type
data = [[10,20,30],["F",'M',"N"]]

df = pd.DataFrame(data)
print(f'df =>\n{df}')
print(f'df.index =>{df.index}')
print(f'df.colums =>{df.columns}')
print(f'df.shape =>{df.shape}')
print(f'df.ndim =>\n{df.ndim}') #차원
print(f'df.dtype =>\n{df.dtypes}') #열마다 타입을 알 수 있다.
print(f'df.values =>\n {df.values}\n {type(df.values)}') #<class 'numpy.ndarray'>
# 넘파이 데이터 => 바로 바로 데이터를 읽어올 수 있는 방법은 / 타입이 똑같은 저장공간에 만들어서
# 리스트로 만들면 주소값으로 찾아가서 값을 찾는것이 아니라, 배열에 입력을 하면 바로 데이터에 입력을 해야한다.
# 타입이 같아야한다면, 인트형 10개의 숫자라면 한 개씩 4바이이트 총 40바이트/ 
# 타입이 다르면 읽는 방식이 다르다. 
# 포인트로 써서 동적으로 쓴다.
# 크기가 정해져있을때는 
# 파이썬은 동적으로 할당하기 때문에, 넘파이라고한다.

# 데이터 => dict 데이터 사용
data = {"name":['홍',"이","박"],"job":["학생","학생"," 주부"]}
df2 = pd.DataFrame(data)

print(f'df =>\n{df2}')

print(f'df2.index =>{df2.index}')
print(f'df2.colums =>{df2.columns}')
print(f'df2.shape =>{df2.shape}')
print(f'df2.ndim =>\n{df2.ndim}') #차원
print(f'df2.dtype =>\n{df2.dtypes}') #열마다 타입을 알 수 있다.
print(f'df2.values =>\n {df2.values}\n {type(df2.values)}') #<class 'numpy.ndarray'>

#Q. 튜터에서 애플 넣었을때, 값이 숫자로 변경되어서 들어가는 것인가? int Yes
#Q  리스트로 만들때는 값들이 행으로 들어가는데, 딕셔너리로 만들면 값이 열방향으로 들어가나요?