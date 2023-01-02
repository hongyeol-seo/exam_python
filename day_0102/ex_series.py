# 인덱스와 라벨(네임) 살펴보기
# - 인덱스 : 판다스 시스템에서 지정하는 ReangeIndex() 정수용 (0.base)
# - 인덱스 라벨(네임) : 시리즈 객체 생성시 지정하는 인덱스

import pandas as pd

# --------------------------------------------
# 시리즈 객체 생성
# 데이터 : 1~20 사시의 3의 배수
# 인덱스 문자 'a' ~ 'f'
# --------------------------------------------

data = list(range(3,21,3))
idx = ["a","b","c","d","e","f"]
idx2 = [11,22,33,44,55,66]
mysr = pd.Series(data, index=idx, name="Jumsu",dtype="float32")
mysr2 = pd.Series(data, index=idx2, name="Jumsu",dtype="float32")

print(mysr) #Name: Jumsu, dtype: int64

#요소읽기 => 변수명[인덱스]
print(f'문자열 {mysr["a"]},{mysr[0]}') #정수형 인덱스가 그대로 간다. 원래 가지고 있다.\
for idx in mysr.index : #길이제고, 레인지잡을 필요없이 속성값을 가지고 있다.
    print(mysr[idx])

#요소 여러개 읽고 싶다 => 변수명[인덱스
print(mysr[["a","d"]],mysr[[0,1,2]])
print(mysr[mysr.index[::2]],mysr[[0,1,2]])

#범위지정요소 읽기
#변수명[시작:끝] => 정수형 인덱스랑 인덱스라벨이랑 이점이 좀 다르다.
#인덱스가 문자열인경우 시작이랑 끝 인덱스까지만 포함
print(mysr["a":"d"],mysr[0:3]) #d포함
print("테스트")
print(mysr["a":"d"],mysr[0]) #d포함

print(mysr2[11],mysr2[0]) #키 에러 0번 / 내가 만든 인덱스가 정수라면 안된다.
# 새로운 인덱스로 주어진다면, 기존에 있었떤 인덱스는 못쓴다.
# 기본 인덱스는 없애버리고, (잘못하면 중복될 수도 있다.)

#데이터를 어떻게 빨리 읽고 빨리 쳐
