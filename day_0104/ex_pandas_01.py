# ------------------------------------
# 연산실습
# ------------------------------------
# 모듈로딩
import pandas as pd

PATH = 'dataFiles\\stock price.xlsx'
df = pd.read_excel(PATH)

print(df)

# [1] 주식ID, 이름, 가격만 사용하도록 데이터 출력
# df = pd.read_csv(PATH , encoding='cp949')
newDF = df[['id','stock_name','price']]
print(newDF)
# [2] 가격에 대한 *100 결과를 추가

print(df.describe()) #통계값
def test(num):

    return format(num, ",")

# newDF['result'] = (newDF['price'] * 100)
newDF['result'] = newDF.price.mul(100,fill_value=0)
newDF['result'] = newDF['result'].apply(test)

print(newDF)

# ==========================================
# index_col
# id 컬럼을 인덱스로 설정하세요.
# 첫번째 : 데이터 파일을 읽을때 설정 => 매개변수(파라미터), index_col
newDF.set_index('id',inplace=True)
print(newDF)

# 특성 컬럼 인덱스로 설정
stockDF = pd.read_excel(PATH,index_col=0)
print(stockDF.index)

#usecols 
#로딩할 특정 컬럼 지정 ==> usecols = ""
stockDF = pd.read_excel(PATH,index_col = 0, usecols="B,D")
print(stockDF.index, stockDF.columns,sep="\n",end="\n\n")
print(stockDF)



# stockDF = pd.read_excel(PATH,skipfooter=3) #아래서 3개
stockDF = pd.read_excel(PATH,skiprows=3,header=None) #해더가 날라간다
stockDF = pd.read_excel(PATH,skiprows=[i for i in range(1,4)]) #해더가 날라간다
stockDF = pd.read_excel(PATH,skiprows=[lambda x : x in range(1,7)]) #해더가 날라간다

print(stockDF)

#컬럼명을 남기고 날리는 방법은 람다를 사용해서 남겨야한다.
# parse_dates 매개변수 => 컬럼지정하면 해당 컬럼의 타입이 datetime64로 변경
# dayfirs 매개변수 : dd m n 월 일 => 일 월로 (True)
# infer_daytime_format 매개변수ㄴㄴㄴㄴㄴㄴ

FILE = 'dataFiles\\banklist.csv'
bankDF = pd.read_csv(FILE,parse_dates=['Updated Date']) #데이터 변환
bankDF = pd.read_csv(FILE,parse_dates=['Updated Date'],dayfirst=True, infer_datetime_format=True) #데이터 변환
print(bankDF)

#date_parser 매개변수 : 직접 날짜시간 포멧 설정 function


#_data_parser lamda x : 

# result2 = list(map((lambda x: ))) 
# print(result2)


from datetime import datetime

print("==============================")
_data_parser = lambda x : datetime.strptime(x,'%d-%b-%y') #시간이 없으면 00시 00분이라도 찍어줘야하는데. #받을려고하는 형태만
#구분자 #파악

bankDF = pd.read_csv(FILE,parse_dates=['Updated Date'],date_parser=_data_parser)
print(bankDF.head(10))

# 내가 포멧을 정해서 만들겠다. 그런데 만약에 지정하지 않는다면 parse_dates 에서 알아서 만들어준다. 
# listOfLambdas = [lambda i=i: i for i in range(1, 6)]
# print(list(map(listOfLambdas)))
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior


stockDFtest = pd.read_excel(PATH) #해더가 날라간다
print(stockDFtest)
stockDFtest = pd.read_excel(PATH,skiprows=list(map(lambda x : x, list(range(5,10))))) #해더가 날라간다
print(stockDFtest)

stockDFtest = pd.read_excel(PATH,skiprows=lambda x: x in [0, 2]) #해더가 날라간다
print(f'stockDFtest => {stockDFtest}')



print(lambda x: x in [0, 2])