# 시리즈 
# pandas.Series()
# 속성() 인덱스, 벨류, ndis, shape
# =========================================
# 데이터 => 리스트 데이터

#Series 객체 속성 출력 함수

def printSeries(srobj,srojbname):
    print(f'{srojbname} =================\n{srobj}')
    print("-------------------------------------")
    print(srobj.index) #Index(['name', 'age', 'loc'], dtype='object')
    print(srobj.values)
    print(srobj.ndim) #차원
    print(srobj.shape)
    print(srobj.dtype)

# __name__ 매직 변수, 시스템에 값을 설정
# 해당 파이썬 파일이 실행중이라면 변수안에 
# 해당 메인이라면 "__main__"
# 다른 파이썬에서 들어온다면

print(f'__name__의 값은? : {__name__}')

if __name__ == "__main__" :

    import pandas as pd
    # 이중 3중 임포트 되니까, 여기에 한꺼번에 잡아 넣는다.

    sr = pd.Series([10,20,30])
    printSeries(sr,"sr")
    # print(sr.__dict__)

    #데이터 딕셔너리
    sr2 = pd.Series({"name":"홍열","age":32,"loc":"Seoul"})
    printSeries(sr2,"sr2")

    # (3) 데이터 => 튜플 형태 데이터
    sr3 = pd.Series((11,22))
    # print(f'sr3 =====\n{sr3}')
    # print("----------")
    # print(sr3.index) #Index(['name', 'age', 'loc'], dtype='object')
    # print(sr3.values)
    # print(sr3.ndim) #차원
    # print(sr3.shape)
    printSeries(sr3,"sr3")


