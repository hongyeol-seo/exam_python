# 모듈과 패키지 살펴보기
# [조건] 동일한 목표/목적으로 구성됨
# 모듈 : 변수, 함수 , 클래스를 하나의 파일로 묶은 것
# 패키지 : 모듈들을 하나로 묶은 것
# 사용법
# 모듈안의 모든 것을 포함
# import 모듈병 => 모듈병. 변수명, 모듈명. 함수
# import 모듈병 as 별칭 => 별칭.변수명
# 모듈안에서 선택한 것만
# from 모듈병 import 변수, 함수, 클래스 / 변수명, 함수, 클래스

# 상속처럼 오버라이딩 할 수 있는가?
# 변수값은 상수인가?

# 파이썬 기본제공 모듈 => 표준모듈

# _ 언더바 하나는 비공개로 쓰지 않겠다.

# import math as m #모듈전체포함 / 모듈명을 찍어야하는것이고
# from math import pow #모듈에서 선택한 것만 포함
import random as r
from math import *
import os  # /모듈명을 찍을 필요가 없다

# print(m.pi)
# print(m.factorial(5)) #모듈.함수명()
print(pow(2, 3))  # 그냥 바로 함수명
print(factorial(5))  # from import 함수명

# 임의의 수 생성 관련 모듈 사용

for _ in range(10):
    print(r.randint(1, 45), end=" ")

# r.random() #01 ~ 1사이 실수
# 범위 위치 지정

# 범위를
print(r.randrange(1, 10, 2))

# mylotte\

arr = []
while True:
    x = r.randint(1, 46)
    if x in arr:
        continue
    if len(arr) == 6:
        break
    arr.append(x)

print(f'행운의 번호 {sorted(arr)} ')

# set을 사용하자


# for i in range(50):
#     print(r.randrange(1,46),end=" ")


s1 = set([1, 2, 3, 4, 5, 6])
s2 = {1, 2, 3, 4, 5, 6}
s3 = (1, 2, 3, 4, 5)

print(s1)
print(s2)
print(type(s3))

# 파일 입출력에서 open이랑 많이 사용됨

FILE_NAME = "Good.txt"
if not os.path.exists(FILE_NAME):
    print("존재하지 않는 파일이다.")
else:
    f = open(FILE_NAME, mode="r", encoding="utf-8")
    print(f.read())
    f.close()
