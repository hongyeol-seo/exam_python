import pandas as pd
# ------------------------------------------------------
# 정렬(sort)
# - 인덱스 기준 정렬 => 오름차순(작은숫자==> 큰 숫자)
# - 데이터 기준 정렬 => 오름차순(작은숫자==> 큰 숫자)
# ------------------------------------------------------
# 모듈/패키지

df1 = pd.DataFrame({'name':['마징가',"베트맨","원더우먼"],
                    'kor':[87,91,69],
                    'eng':[99,73,89],
                    'sci':[71,95,62]})

print(df1)

# [1] 인덱스 기준 정렬 => 내림차순
desDF = df1.sort_index(ascending=False) #행기준 / 내림차순
print(desDF.index,desDF,sep="\n",end="\n\n")

#열 기준, 내리차순
colDesDF = df1.sort_index(axis=1,ascending=True) #열기준 / 내림차순
print(colDesDF.index,colDesDF,sep="\n",end="\n\n")

# 데이터 즉, 즉 값 기준 정렬 => 내림차순
# DataFrame.sort_values()
df2 = df1.sort_values(by=['name'],ascending=False)
print(df2,end="\n\n")

df2 = df1.sort_values(by=['kor',"eng"],ascending=False)
print(df2,end="\n\n")

# df.sort_values(by='col4', key=lambda col: col.str.lower())
#    col1  col2  col3 col4
# 0    A     2     0    a
# 1    A     1     1    B
# 2    B     9     9    c
# 3  NaN     8     4    D
# 4    D     7     2    e
# 5    C     4     3    F

#이름 컬러만 뺀다면?
print("="*50)
print(df2['name'],df2.name,sep="\n")
print("="*50)

df2.name =['B-Man','maziga','Woman']
print("="*50)
print(df2['name'],df2.name,type(df2.name),sep="\n")
print("="*50)

print(df2.name[1],type(df2.name[1])) 
# 원래 가지고 있던 인덱스를 가지고 가서 섞여버린다.
# 그래서 깨끗하게 가져오고싶다면, igore인덱스를 가져와야한다.

print(df2.name[1].lower()) 


#연습하기
# df1.name =['B-Man','maziga','Woman']
# print(df1.name)
# print(type(df1.name[0]))
# print(df1.name[0].upper())
# print(df1.columns[1].upper())