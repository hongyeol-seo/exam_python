import random as r
import pandas as pd

# 1. 시리즈 데이터 생성 후 데이터를 출력해주세요.
# 데이터 1~100 사이 임의의 숫자 30개로 구성

arr = list()

while True :
    arr.append(r.randint(1,100))
    if len(arr) == 30:
        print(pd.Series(list(arr)))
        break

# 2. 시리즈 데이터를 생성 후 정보를 출력해주세요.
# 데이터 1~100 사이 임의의 숫자 30개로 구성
# 조건 : 중복된 숫자 없음

arr = set()

while True :
    arr.add(r.randint(1,100))
    if len(arr) == 30:
        print(pd.Series(list(arr)))
        break

# count = 1
# while count <= 30:
#     x = r.randint(1, 100)
#     if x not in arr :
#         arr.add(x)
#         count += 1


# 3. 시리즈 데이터를 생성 후 정보를 출력해주세요. 
# 데이터 0.0 ~ 1.0 사이 살시 데이터 10개로 구성

arr = []
for i in range(10):
    arr.append(round(r.random(),2))

print(sorted(arr))