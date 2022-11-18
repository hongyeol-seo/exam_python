# 1. 3, 6, 9 게임을 파이썬으로 구현해 보세요.

msg = int(input("숫자를 입력하세요 : "))

for i in range(1, msg+1) :

    n = str(i)
    count = 0 
    for x in n :

  
        if ('3' in x) or ('6' in x) or ('9' in x) :
            count += 1


    if count != 0 : 
        print(count* 'X', end=" ")


    else : 
        print(i, end=" ")