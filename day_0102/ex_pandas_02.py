#모듈로딩

import pandas as pd #데이터 분석용 패키지
import ex_pandas as mp #나의 모듈

# Series객체의 요소 다루기 => 인덱스 사용
# [사용법] 객체 변수명[인덱스]

data = list(range(5,31,5))
sr1 = pd.Series(data)

#요소 읽기 => 변수명 

print("================================================")
print(f'sr[0] => {sr1[0]},{type(sr1[0])}')
print(f'sr[0] => \n{sr1[0:5:2]},{type(sr1[0])}') 
print("================================================")

for idx in range(len(sr1)):
    print(f'sr[{idx}] => {sr1[idx]},{type(sr1[idx])}')

# 요소 여러개 읽기
# ---> 결과 데이터가 시리즈 / 원소 한 개씩 빼오면, 원래 자기값이 나온다.

print(f'sr[[0,4]] => \n{sr1[[0,4]]},{type(sr1[[0,4]])}') #시리즈타입
print(f'sr[[0,4]] => \n{sr1[[1]]},{type(sr1[[1]])}') #시리즈타입
print(f'sr[[0,4]] => \n{sr1[[1]]},{type(sr1[[1]])}') #시리즈타입 #인덱스를 리스트에 담아서

# 요소 범위 지정하여 읽기 => 변수명[시작:끝+1]
print(f'sr[0부터 4번 요소가져오기] => \n{sr1[0:5:2]},{type(sr1[0:5:2])}') 
print(f'sr[0] => \n{sr1[0:5:2]},{type(sr1[0])}') 

for idx in sr1.index:
    print(f'{idx}')


    