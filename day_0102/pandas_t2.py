import pandas as pd
import random as r


def printSeries(srobj,name):
    print(f"==========={name}==============")
    # Index(['name', 'age', 'loc'], dtype='object')
    print(srobj)
    print(f'인덱스 {srobj.index}')
    print(f'값 {srobj.values}')
    print(f'차원 {srobj.ndim}')  # 차원
    print(f'형태 {srobj.shape}')
    print(f'디타입 {srobj.dtype}')
    print(f'타입 {type(srobj)}')

# arr = set()
# count = 1
# while count <= 30:
#     x = r.randint(1, 100)
#     if x not in arr :
#         arr.add(x)
#         count += 1

# print(arr)
# print(len(arr))

# sr2 = pd.Series(list(arr))
# print(sr2)

# sr = pd.Series([10, 20, 30])
# printSeries(sr,"sr")

# sr2 = pd.Series({"name": "홍열", "age": 32, "loc": "Seoul"})
# printSeries(sr2,"sr2")

# sr3 = pd.Series((11,22,))
# printSeries(sr3,"sr3")


data = list(range(5,31,5))
sr1 = pd.Series(data)

# print(f'sr[0] => {sr1[0]}')
# print(f'type(sr[0]) => ,{type(sr1[0])}')

# for idx in range(len(sr1)):
#     print(f'sr[{idx}] => {sr1[idx]},{type(sr1[idx])}')

#여러개의 요소값 읽기
print(f'sr[4] => \n{sr1[4]},{type(sr1[4])}') 
print(f'sr[[0,4]] => \n{sr1[[0,4]]},{type(sr1[[0,4]])}') 
print(f'sr[0:5] => \n{sr1[0:5:2]},{type(sr1[0:5:2])}') 


data = list(range(3,21,3))
idx = ["a","b","c","d","e","f"]
idx2 = [11,22,33,44,55,66]
mysr = pd.Series(data, index=idx, name="Jumsu",dtype="float32")
mysr = pd.Series(data, index=idx, name="Jumsu")

# print(mysr)

# print(f'문자열 인덱스 : {mysr["a"]},{mysr[0]},{type(mysr["a"])}')
# print(f'문자열 인덱스 여러 값 읽기\n{mysr[["a","d","c"]]}\n,{mysr[[0,1,2]]}\n,{type(mysr[["a","d","c"]])}')
# print(mysr[mysr.index[::2]],mysr[[0,1,2]])

data = list(range(3,21,3))
idx2 = [11,22,33,44,55,66]
mysr2 = pd.Series(data, index=idx2, name="Jumsu",dtype="float32")

print(mysr2[11])