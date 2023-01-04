# -------------------------------------------------
# 데이터 분석 => 기초 통계 함수, 고유값, 결측치
# -------------------------------------------------

import pandas as pd

FILE = r'dataFiles\auto-mpg.csv'

# 데이터 정보 확인 함수 ----------------------------
def printDataInfo(df):
    df.info()
    print(df.head(),df.tail(),sep="\n",end="\n\n")
    print(df.describe(),end="\n")
    print(f'Index => {df.index}\nColums => {df.columns}',end="\n\n")
# (1) 데이터 읽기
mpgDF=pd.read_csv(FILE, header=None)

# (2) 데이터 확인
printDataInfo(mpgDF)

# (3) 칼럼명 추가
# 1. mpg: continuous
# 2. cylinders: multi-valued discrete
# 3. displacement: continuous
# 4. horsepower: continuous
# 5. weight: continuous
# 6. acceleration: continuous
# 7. model year: multi-valued discrete
# 8. origin: multi-valued discrete
# 9. car name: string (unique for each instance)

# 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name'
# 컬럼명 넣기

mpgDF.columns =['mpg', 'cylinders' ,'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']

# (4) 실제 데이터와 타입
print(mpgDF.horsepower.dtype)
#마력 타입 바꾸기

# mpgDF.horsepower.astype('float')
# print(mpgDF.horsepower.dtype)

# could not convert string to float: '?'
# 그 안에 물음표가 있었던거야. 

# 마력 안에 => 데이터 값 중 '?'이 있다.
# 그래서 찾아서 해결을 해야한다. 
# (4-1) 해당 컬럼의 데이터 종류 확인
# (4-2) 해당 컬럼의 데이터 종류별 갯수 확인 (unique) 해당컬럼에 값이 몇 개있는가

horseUnique = mpgDF.horsepower.unique()
print('horsepower :',horseUnique)
horseValueCount = mpgDF.horsepower.value_counts()
print('horsepower :',horseUnique)
# print(horseValueCount['?']) #? 시리즈 안에 있느것 찾기
# mpgDF = mpgDF.astype({'horsepower':'float'})
# print(mpgDF.horsepower.dtype)

# ? 가 몇 개인지 어떻게 찾는가?

