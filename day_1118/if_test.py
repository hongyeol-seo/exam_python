msg = input("데이터를 입력해주세요 : ").strip()

if msg : 
    print("OK")

else :
    print("데이터 없음")

# [실습] ----------------------------------------------------
# 정수 데이터 입력 받은 후 정수만큼 *찍기

str = (input("정수를 입력해주세요").strip())
#숫자가 아니면 ?  / 에러를 발생시키면 안되고, 

if len(str) > 0 :
    if str.isdecimal()   :
        print('*'*int(str))
    else : 
        print("정수를 입력하세요.")
else :
    print(f'다시 입력해주세요')


