# ---------------------------------------
# #CSV FILE ==> DataFrame 객체로 저장 
#-pandas.read_csv
# ---------------------------------------

import pandas as pd

FILE = 'dataFiles\\banklist.csv'

PATH = '20220930.csv'
df = pd.read_csv(PATH , encoding='cp949')
print(f'bankDF====>\n{df}')
df.info()
print(df.head(50))


# DF 객체 생성 --------------------------------------
backDF = pd.read_csv(FILE)
print(f'bankDF====>\n{backDF}')

#DF 데이터 확인용 메서드 --------------
# [1] 전체 요약 정보 제공 메서드 => info
backDF.info() #555 entries 555행 / 555레코드 / 


# [2] 앞부분 5줄(기본값) 실제 데이터 보기 => head(n)메서드 
# 끝부분
# print(backDF.head(),sep="\n\n")
# print(backDF.tail())


# [3] 데이터에 기술통계 적용한 결과 제공 => 데이터의 분포 확인 => describe
# 수치데이터만 가능 / 그런데 나는 모든 데이터를 보고 싶다? (inclode )
# print(backDF.describe())

#std 편차
#편차가 클수록 흩어져잇찌

# print(backDF.describe(include='all'))

#데이터 가지고 놀기 =================================
print(f'backDF.colums=>{backDF.columns}')

# (1) 4개 컬럼 = >Bank Name, City, Closeing Date, Update Date
newDF = backDF[['Bank Name','City','Closing Date',"Updated Date"]]
print(newDF.info())
print(newDF.head(3))

# (2) 컬럼 중에서 인덱스로 설정 (원하는 것)
newDF.set_index(['Bank Name','City'],inplace=True)
print(newDF.index, newDF.columns,sep="\n",end="\n\n")
print(newDF.head(3))

# (3) Update Date 기준으로 가장 최근 날짜부터 보여주세요.
# datetime으로 바꿔야한다.
newDF.sort_values(by=['Updated Date'],key=lambda col:pd.to_datetime(col),ascending=False,inplace=True)
print(newDF['Updated Date'].values)
#문자가 아니라, 날짜로 바꿀 수 있어야한다.

pd.to_datetime('20-Dec-17')

# def ymd(date):
#     result = datetime.strptime(date[:-2]+'20'+date[-2:], '%d-%b-%Y').strftime('%Y-%m-%d')
#     return result

# b['Updated Date']=b['Updated Date'].apply(ymd)

pd.to_datetime('23-Oct-17')
pd.to_datetime('17-Oct-23')
pd.to_datetime('Oct-23-17')
pd.to_datetime('23-17-Oct')

# https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-strptime-behavior

