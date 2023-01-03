# -------------------------------------
# Series 데이터 연산 수행
# 브로드캐스팅(Broadcasting) : 
# 연산 수행되는 SR/DF에 동일 크기로 확장해서 연산 수행 
# -------------------------------------
import pandas as pd

# SR 객체 생성
sr1 = pd.Series([11,12,13,14,15])
print(sr1)

#연산 수행 =(1) Series 연산자 숫자 =================
sr2 = sr1 + 10
print(f'sr1 + 10 :=>\n{sr2},end=\n\n')
#시리즈의 갯수만큼 만들어져서
#매칭되는 값만큼 더해진다.

sr2 = sr1 - 10
print(f'sr1 - 10 :=>\n{sr2},end=\n\n')

sr2 = sr1 * 10
print(f'sr1 * 10 :=>\n{sr2},end=\n\n')

sr2 = sr1 / 10
print(f'sr1 / 10 :=>\n{sr2},end=\n\n')


sr2 = sr1 > 13
print(f'sr1 > 10 :=>\n{sr2},end=\n\n')

sr2 = sr1 != 13
print(f'sr1 > 10 :=>\n{sr2},end=\n\n')

#연산 수행 - (2) Series 연산자 Series
sr3 = pd.Series([7,7,7])

sr4 = sr1 + sr3
print(f'sr1 + sr3 :=>\n{sr4},end=\n\n')

#연산을 할 자리에 없으면 NaN
#연산 수행 : (3) Series. 연산메서드
#빈데이터 값을 채운 후 연산가능

sr4 = sr1.add(sr3,fill_value=0)
print(f'sr1 + sr3 :=>\n{sr4},end=\n\n')


# 결측치와 비교불가
# sr4 = sr1 >= sr3
# print(f'sr1 + sr3 :=>\n{sr4},end=\n\n')
