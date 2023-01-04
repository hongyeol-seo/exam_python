# -----------------------------------------
# 인덱스(Index) 다루기
# -----------------------------------------
# 모듈/패키지 로딩 -------------------------
import pandas as pd

# df 생성 ---------------------------------
df1 = pd.DataFrame

# DF객체 생성 --------------------------------
df1 = pd.DataFrame({'name':['마징가',"베트맨","원더우먼"],
                    'kor':[87,91,69],
                    'eng':[99,73,89],
                    'sci':[71,95,62]})

# DF데이터 확인하기
print(f'======================================\n{df1}')
print(f'df1.index => {df1.index}')
print(f'df1.colums => {df1.columns}')

# [1] 특정 컬럼을 행 인덱스로 설정 ===========================
# ex) 이름, 유니크한, 
# DadaFrame.set_index()
# name' 컬럼을 행 인덱스로 설정
nameDF2 = df1.set_index('name')
print(nameDF2)

#모든 행의 데이터 값을 출력 DF.loc[행인덱스]
for i in nameDF2.index:
    print(i, nameDF2.loc[i],sep='\n',end="\n\n") #시리즈

print("--------------------------------")
sr1 = nameDF2.loc["마징가"]
print(type(sr1),sr1,sep='\n')

# [2] 인덱스 부분 변경
# 전체 변경 => DF.index=[새로운 인덱스],DF.colums=[새로운 인덱스]
# DataFrame.rename() 메서드

# 행인덱스 '마징가','베트맨','원더우먼' ==> '베트맨' ----> '홍길동'
copyDF = nameDF2.rename(index={'베트맨':'홍길동'})
print("****************************************")
print(copyDF, end="\n\n")
print("****************************************")


df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)


#열(column) 인덱스 변경
df.rename(columns={'B':"BB"},inplace=True) #반환값없음
print(df)

#행(row) 인덱스를 변경
#10 20 30으로 변경

df.rename(index={0:00,1:11,2:22},inplace=True)
print(df.index)
print(df)

#행(row) 인덱스 변경 => 10,20,30 => '10','20','30' 변경
df.rename(index={00:"10",11:"11",22:"20"},inplace=True)
print(df.index)

df.rename(index=str,inplace=True)

#[3] 새로운 인덱스 지정 설정 =============================
#DataFrame.reindex([새로운 인덱스])
# => 기존 인덱스가 아닌 인덱스의 값은 존재 하지 않는다 => NaN not a Number
newdf = df.reindex(['10','15','20','25'])
newdf = df.reindex(['10','15','20','25'],method='bfill')
#nan => 결측치, 

print('변경된 인덱스 DF=>',df,end="\n")
print('변경된 인덱스=>',newdf,end="\n")

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html

#NaN 값을 내가 원하는 값으로 채우기 => fill_value=값

newdf = df.reindex(['10','15','20','25'],fill_value=100)
print('변경된 인덱스=>',newdf,end="\n") #결측치는 채워야한다.

#★메소드를 쓸때마자 메소드 API를 봐야한다.★★★★★★

#[4] 판다스에서 지정하는 기본 인덱스로 초기화
# DataFrame.reset_index()
# 기존 인덱스 ==> 컴으로 추가 됨/.
newdf2 = newdf.reset_index()
print(newdf2)

newdf3 = newdf2.reset_index()
print(newdf3)
